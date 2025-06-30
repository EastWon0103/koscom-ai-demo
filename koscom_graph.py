from langgraph.graph import StateGraph, START
from State import State
from openai_chatbot import chatbot
from sql_agent import sql_agent


#https://wikidocs.net/261598 -> 분기처리 하는 거 확인
def use_sql_agent(state: State):
    pass

def get_graph():
    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_node("sql_agent", sql_agent)


    graph = graph_builder.compile()

    return graph

if __name__ == '__main__':
    graph = get_graph()
    graph.get_graph().draw_mermaid_png(output_file_path="./graph.png")