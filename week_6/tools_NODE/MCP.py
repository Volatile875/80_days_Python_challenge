from langgraph.graph import StateGraph, START
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()  # Load environment variables from .env file

# Use a local Ollama model (make sure Ollama is running locally)
llm = ChatOllama(model="llama3.1:8b")  # or use another model you have: "mistral", "neural-chat", etc.

# Define a sample tool
@tool
def calculator(operation: str, a: float, b: float) -> float:
    """Perform add, subtract, multiply, divide, or modulus operations."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else None
    elif operation == "modulus":
        return a % b if b != 0 else None
    else:
        return None

# MCP client for local FastMCP server
client = MultiServerMCPClient(
    {
        "arith": {
            "transport": "stdio",
            "command": "python3",          
            "args": ["/Users/nitish/Desktop/mcp-math-server/main.py"],
        },
        "expense": {
            "transport": "streamable_http",  # if this fails, try "sse"
            "url": "https://splendid-gold-dingo.fastmcp.app/mcp"
        }
    }
)


tools = [calculator]

llm_with_tools = llm.bind_tools(tools)

# state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def build_graph():

    # nodes
    async def chat_node(state: ChatState):

        messages = state["messages"]
        response = await llm_with_tools.ainvoke(messages)
        return {'messages': [response]}

    tool_node = ToolNode(tools)

    # defining graph and nodes
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    # defining graph connections
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    chatbot = graph.compile()

    return chatbot

async def main():
    try:
        chatbot = build_graph()

        # running the graph
        result = await chatbot.ainvoke({"messages": [HumanMessage(content="Find the modulus of 132354 and 23 and give answer like a cricket commentator.")]})

        print(result['messages'][-1].content)
    finally:
        # ChatOllama owns an async HTTP client that must close before asyncio.run exits.
        await llm._async_client.close()

if __name__ == '__main__':
    asyncio.run(main())
