from langchain_core.messages import SystemMessage ,HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv 
import os

load_dotenv()


model = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)
chat_model = ChatHuggingFace(llm=model)


messages = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="Can you tell me something about transformers?"),

]

AI_Message=AIMessage(content="Transformers are a type of neural network architecture that has revolutionized natural language processing. They use self-attention mechanisms to process input data, allowing them to capture long-range dependencies and context effectively. This architecture has been the basis for many state-of-the-art models in NLP, such as BERT and GPT.")


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
