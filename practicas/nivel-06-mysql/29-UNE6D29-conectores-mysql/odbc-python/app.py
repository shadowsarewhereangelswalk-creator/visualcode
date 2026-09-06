import os
import pyodbc

dsn = os.getenv("MYSQL_ODBC_DSN", "MySQLUne6D29")
connection = pyodbc.connect(f"DSN={dsn}")

query = """
SELECT contact_id, full_name, email, city, created_at
FROM contacts
ORDER BY contact_id
"""

with connection:
    cursor = connection.cursor()
    cursor.execute(query)
    for contact_id, full_name, email, city, created_at in cursor.fetchall():
        print(f"{contact_id} | {full_name} | {email} | {city} | {created_at}")

connection.close()
