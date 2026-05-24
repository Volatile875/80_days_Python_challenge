from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='what are the 5 interesting facts about {topic}',
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational"
)  

model = ChatHuggingFace(llm=llm)

chain = prompt | model | StrOutputParser()

result = chain.invoke({ 'topic': 'cricket' })

print(result)