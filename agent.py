import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import pymysql

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('api_key')

db_user = "root"
db_password = "password"
db_host = "127.0.0.1"
db_port = 3306
db_name = "chatbot_test_db"
DB = SQLDatabase.from_uri("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            db_user, db_password, db_host, db_port, db_name
    ))

LLM = ChatOpenAI(model_name="gpt-3.5-turbo")
toolkit = SQLDatabaseToolkit(db=DB, llm=LLM)

agent_executor = create_sql_agent(
    llm=LLM,
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("Describe the table test to me and what information is stored in it")

def agent(query: str):
    return {"agent": query }