import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

# Establish connection
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_ca="ca.pem"
    )
def initialize_table():
    # get connection
    conn = get_connection()
    # Create a cursor object
    cursor = conn.cursor()
    #create tables
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(20) PRIMARY KEY,
                password VARCHAR(20)
            )
            """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                username VARCHAR(20) PRIMARY KEY,
                time_spent DECIMAL(16, 7),
                score int,
                attempt int,
                FOREIGN KEY (username) REFERENCES users(username)
            )
            """)
    cursor.close()
    conn.close()

if __name__ == "__main__" :
    initialize_table()