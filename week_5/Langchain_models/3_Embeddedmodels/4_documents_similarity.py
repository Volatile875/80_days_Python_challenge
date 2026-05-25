from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",)


documents=["GG is my favourite cricket player and i love how he approach the games.",
           "I am not a fan of cricket but i like watching football.",
           "I am a die hard fan of football and i love watching football.",
           "RCB is the worst team ever in the ipl History."]


query = "tell me about RCB"


doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

score = cosine_similarity([query_embedding], doc_embeddings)[0]

print(list(enumerate(score)))