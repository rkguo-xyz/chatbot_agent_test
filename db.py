# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, text

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'chatbot_test_db'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
	return create_engine(
		"mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
	)

def database_exists(engine, db_name):
    """Check if a specified database exists."""
    with engine.connect() as conn:
        existing_databases = conn.execute(text("SHOW DATABASES;"))
    # conn.close()
    return db_name in [d[0] for d in existing_databases.fetchall()]

def create_database(engine, db_name):
    if not database_exists(engine, db_name):
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            conn.execute(text("COMMIT"))


if __name__ == '__main__':
	try:
        # Use an engine without a specific database to execute the CREATE DATABASE command
		engine_without_db = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}")
		create_database(engine_without_db, database)
        
        # Now, use your original engine to connect to the new database
		engine = get_connection()
		connection = engine.connect()
		print(f"Database {database} created and connection established.")
		connection.close()
	except Exception as ex:
		print("Operation could not be completed due to the following error: \n", ex)