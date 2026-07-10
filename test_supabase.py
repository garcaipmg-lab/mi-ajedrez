import os
import psycopg2

print("Iniciando prueba de conexión...")

try:
    # Obtenemos la variable de entorno que configuraste en Render
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if not DATABASE_URL:
        print("❌ ERROR: La variable DATABASE_URL no está configurada en Render.")
    else:
        print(f"✅ Intentando conectar a: {DATABASE_URL[:20]}...") # Imprimimos solo el inicio por seguridad
        conn = psycopg2.connect(DATABASE_URL)
        print("¡ÉXITO! La conexión con Supabase funciona perfectamente.")
        conn.close()
        
except Exception as e:
    print(f"❌ ERROR CRÍTICO DE CONEXIÓN: {e}")
