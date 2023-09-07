# LangChain Agent test repo
The agent can query local database using natural language
### Prereqs
- install mysql
- mysql server must run on localhost 127.0.0.1 port 3306
- must have user "root" and password "password"
- must have a database named "chatbot_test_db"
### Python deps
- langchain
- pymysql
- python-dotenv
- sqlalchemy (for creating database)