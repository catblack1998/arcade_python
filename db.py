import mysql.connector
import streamlit as st

def obtener_conexion():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        port=st.secrets["mysql"]["port"]
    )

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

def registrar_usuario_db(username, password):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        # Registra un usuario nuevo empezando desde el nivel 0 (Encuesta) y con 0 monedas
        cursor.execute(
            "INSERT INTO usuarios (username, password, monedas, nivel_actual) VALUES (%s, %s, 0, 0)",
            (username, password)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        # Si el usuario ya existe, dará error de duplicado
        return False

def actualizar_progreso_db(username, monedas, nivel, exp="", meta="", que_es=""):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE usuarios 
               SET monedas = %s, nivel_actual = %s, resp_experiencia = %s, resp_meta = %s, resp_que_es = %s 
               WHERE username = %s""",
            (monedas, nivel, exp, meta, que_es, username)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar datos: {e}")
