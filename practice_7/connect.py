#1 - Database connection
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="phonebook",
        user="testuser",
        password="1234",
        host="localhost",
        port=5432
    )
    conn.set_client_encoding('UTF8')
    cur = conn.cursor()
    print("Database connected successfully!")

except Exception as e:
    print("Error:", e)



