from tempfile import template
from langchain_core.messages import SystemMessage ,HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
import os

load_dotenv()


# Get token
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize model
llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)



chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)