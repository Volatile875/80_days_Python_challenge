from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

# Directly pass model name
model = OllamaLLM(model="llama3.1:8b", temperature=2.0)

result = model.invoke("Suggest me 5 Indian male names?")

print(result)

