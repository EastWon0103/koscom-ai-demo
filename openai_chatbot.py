from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from State import State

load_dotenv()

llm = init_chat_model("openai:gpt-4.1")
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}