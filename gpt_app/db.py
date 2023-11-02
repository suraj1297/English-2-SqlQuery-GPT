import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='order'
    )

def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except mysql.connector.errors.ProgrammingError as e:
        cursor.close()
        return f"Error: {e.msg}"
    else:
        data = cursor.fetchall()
        cursor.close()
        return data
