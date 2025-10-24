import mysql.connector

# Establish connection
def get_connection():
    return mysql.connector.connect(
        # mysql --user avnadmin --password=AVNS_qtZJ9vmH7WB4FmxQnrK --host mysql-1699fc57-abcd80g-543f.i.aivencloud.com --port 26617 defaultdb
        host="mysql-1699fc57-abcd80g-543f.i.aivencloud.com",       # or your cloud DB host
        port=26617,
        user="avnadmin",
        password="AVNS_qtZJ9vmH7WB4FmxQnrK",
        database="defaultdb",
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