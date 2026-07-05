import mysql.connector
import streamlit as st

def obtener_conexion():
    # Streamlit leerá automáticamente el archivo secrets.toml localmente
    # Y en la web leerá la configuración de la nube
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        port=st.secrets["mysql"]["port"]
    )

# ... El resto de tus funciones (verificar_usuario y actualizar_progreso_db) se quedan EXACTAMENTE IGUAL ...

def verificar_usuario(username, password):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario
    except Exception as e:
        return None

def actualizar_progreso_db(username, monedas, nivel):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET monedas = %s, nivel_actual = %s WHERE username = %s",
            (monedas, nivel, username)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar datos: {e}")
