import psycopg2

conn = psycopg2.connect(
    host="34.21.95.193",
    port=5432,
    database="postgres",  # ← este es el nombre correcto
    user="postgres",
    password="adminUNI123!"
)
print("Conexión exitosa!")
conn.close()