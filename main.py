from psycopg2 import connect

db = connect(host="localhost", port="5432", user="postgres",
             password="lagranzanahoriavendra")

print(db)

print("Hello World")
