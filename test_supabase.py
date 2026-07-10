import psycopg2

# Pega aquí tu URL completa (la que copiamos de Supabase)
DATABASE_URL = "postgresql://postgres:3JC94Nu5GzIpsDbM@db.stizpdyftzoeuwigxgbi.supabase.co:5432/postgres"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("¡CONEXIÓN EXITOSA! Ya podemos hablar con la base de datos.")
    conn.close()
except Exception as e:
    print("Error de conexión:", e)