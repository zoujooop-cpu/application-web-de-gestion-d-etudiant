import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="etudiant_db",
    user="postgres",
    password="AJP.670"
)

cursor = connection.cursor()