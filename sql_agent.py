from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

# MySQL 접속 URL
db_url = "mysql+pymysql://root:root@localhost:3306/glossary_db"

# SQLDatabase 객체 생성
db = SQLDatabase.from_uri(db_url,
              include_tables=["GLOSSARY"],
              sample_rows_in_table_info=3)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# SQL Agent 생성
sql_agent = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True,
    return_intermediate_steps=True
)

# Query 실행 도구
@tool
def db_query_tool(query: str) -> str:
    """
    Run SQL queries against a database and return results
    Returns an error message if the query is incorrect
    If an error is returned, rewrite the query, check, and retry
    """
    # 쿼리 실행
    result = db.run_no_throw(query)

    # 오류: 결과가 없으면 오류 메시지 반환
    if not result:
        return "Error: Query failed. Please rewrite your query and try again."
    # 정상: 쿼리 실행 결과 반환
    return result
## https://wikidocs.net/270692 확인하고 수정하기

# 자연어 질의
if __name__ == '__main__':
    print(db.table_info)
    question = "체결의 약자 좀 알려줘"
    response = sql_agent.invoke(question)

    print("\n🧠 LLM 기반 응답:")
    print(response)