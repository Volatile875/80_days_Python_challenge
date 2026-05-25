from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension= 32)

documents = [
    "New Delhi is the capital of India",
    "The capital of India is New Delhi",
    "Kolkata is the capital of West Bengal",
    "The capital of england is london."
    ]

result = embeddings.embed_query('New Delhi is the capital of India')

print(str(result))