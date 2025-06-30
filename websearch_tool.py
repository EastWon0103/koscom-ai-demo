from langchain_core.tools import tool
from langgraph.types import interrupt, Command
from langchain_community.retrievers import TavilySearchAPIRetriever

retriever = TavilySearchAPIRetriever(k=3)
def web_search(input: str):
    return retriever.invoke(input)
