import streamlit as st
from encuesta import mostrar_encuesta
import nivel1
import nivel2
import db  # <-- Importamos el nuevo módulo de base de datos

st.set_page_config(page_title="Arcade Python", page_icon="🎮", layout="centered")

# 1. Control del estado del Login en la memoria del navegador
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""

# --- PANTALLA DE LOGIN ---
if not st.session_state.autenticado:
    st.title("🔒 Acceso al Servidor Arcade")
    st.subheader("Por favor, inicia sesión para continuar tu entrenamiento")
    
    usuario_input = st.text_input("Usuario:")
    password_input = st.text_input("Contraseña:", type="password")
    
    if st.button("Ingresar al Sistema"):
        # Validar contra la base de datos MySQL
        datos_user = db.verificar_usuario(usuario_input, password_input)
        
        if datos_user:
            st.session_state.autenticado = True
            st.session_state.usuario = datos_user['username']
            st.session_state.coins = datos_user['monedas']
            st.session_state.nivel_guardado = datos_user['nivel_actual']
            st.success(f"¡Bienvenido de vuelta, {st.session_state.usuario}!")
            st.rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos. Inténtalo de nuevo.")

# --- PANTALLA DEL JUEGO (SI YA SE LOGUEÓ) ---
else:
    # Barra lateral
    st.sidebar.title("🎮 Panel de Control")
    st.sidebar.write(f"🧑‍💻 Agente: **{st.session_state.usuario}**")
    st.sidebar.markdown(f"## 🪙 Monedas: **{st.session_state.coins}**")
    
    # Botón para cerrar sesión si lo desea
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
        
    st.sidebar.write("---")

    opcion = st.sidebar.radio(
        "Ir a:",
        ["📋 Ganar Monedas (Encuesta)", "🎯 Jugar: Nivel 1 (Hola Mundo)", "⚡ Jugar: Nivel 2 (Variables)"]
    )

    st.title("🚀 Aprende Python - Modo Arcade")

    if opcion == "📋 Ganar Monedas (Encuesta)":
        mostrar_encuesta()
    elif opcion == "🎯 Jugar: Nivel 1 (Hola Mundo)":
        nivel1.mostrar_nivel()
    elif opcion == "⚡ Jugar: Nivel 2 (Variables)":
        nivel2.mostrar_nivel()
