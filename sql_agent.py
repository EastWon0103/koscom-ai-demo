from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

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

# 자연어 질의
if __name__ == '__main__':
    print(db.table_info)
    question = "체결의 약자 좀 알려줘"
    response = sql_agent.invoke(question)

    print("\n🧠 LLM 기반 응답:")
    print(response)