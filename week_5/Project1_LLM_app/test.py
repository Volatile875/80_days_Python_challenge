from typing import Annotated, Literal, Optional, TypedDict

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec

from langchain_core.prompts import ChatPromptTemplate

import os
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

for proxy_var in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
    if os.environ.get(proxy_var) == "http://127.0.0.1:9":
        os.environ.pop(proxy_var)

if "PostgreSQL" in os.environ.get("CURL_CA_BUNDLE", ""):
    os.environ.pop("CURL_CA_BUNDLE")

key = os.getenv("PINECONE_KEY")

if key:
    os.environ["PINECONE_API_KEY"] = key

client = Pinecone(api_key=key)


# ==========================================
# LLM
# ==========================================

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.7
)


# ==========================================
# Structured Output Schema
# ==========================================

class StructuredDocumentOutput(TypedDict):
    document_type: Annotated[
        Literal["budget_speech", "manual", "report", "other"],
        "Best matching category for the document.",
    ]
    title: Annotated[str, "Short title for the document."]
    summary: Annotated[str, "Clear 3-5 sentence summary of the document content."]
    key_points: Annotated[list[str], "Most important points from the document."]
    audience: Annotated[
        Optional[str],
        "Who the document is mainly written for, if clear."
    ]
    tone: Annotated[
        Literal["formal", "technical", "informative", "persuasive", "other"],
        "Overall tone of the document.",
    ]


# ==========================================
# Read PDF
# ==========================================

def read_doc(directory):
    file_loader = PyPDFLoader(directory)
    documents = file_loader.load()
    return documents


# ==========================================
# Chunk PDF
# ==========================================

def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(docs)

    return chunks


# ==========================================
# Embeddings
# ==========================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================
# Load Document
# ==========================================

doc = read_doc("Document/budget_speech.pdf")

chunks = chunk_data(doc)

print(f"Total Chunks Created: {len(chunks)}")


# ==========================================
# Pinecone Index
# ==========================================

index_name = "langchain-vector"

existing_indexes = client.list_indexes().names()

if index_name not in existing_indexes:

    client.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    print("Index Created")

else:
    print("Index Already Exists")


# ==========================================
# Vector Store
# ==========================================

index = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name=index_name,
    async_req=False,
    pool_threads=1
)

print("Documents Stored In Pinecone")


# ==========================================
# Similarity Search
# ==========================================

def retrieve_query(query, k=2):

    matching_results = index.similarity_search(
        query,
        k=k
    )

    return matching_results


# ==========================================
# QA Prompt
# ==========================================

qa_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the question using only the provided document context. "
            "If the answer is not in the context, say you do not know.\n\n"
            "Context:\n{context}",
        ),
        ("human", "{question}"),
    ]
)


# ==========================================
# Retrieve Answer
# ==========================================

def retrieve_answers(query):

    doc_search = retrieve_query(query)

    print("\nRetrieved Chunks:\n")

    for doc in doc_search:
        print(doc.page_content[:300])
        print("=" * 100)

    context = "\n\n".join(doc.page_content for doc in doc_search)

    response = model.invoke(
        qa_prompt.format_messages(
            context=context,
            question=query
        )
    )

    return response.content


# ==========================================
# User Query
# ==========================================

our_query = (
    "How much the agriculture credit target "
    "will be increased by how many crore?"
)

answer = retrieve_answers(our_query)

print("\nANSWER:\n")

print(answer)
