import streamlit as st
from encuesta import mostrar_encuesta
import nivel1
import nivel2
import nivel3  # <-- Importamos el nuevo nivel 3
import db

st.set_page_config(page_title="Arcade Python", page_icon="🎮", layout="centered")

# Inicializar estados de memoria
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ""
if 'menu_actual' not in st.session_state:
    st.session_state.menu_actual = "📋 Ganar Monedas (Entrevista)"

# --- PANTALLA DE ACCESO (LOGIN Y REGISTRO) ---
if not st.session_state.autenticado:
    st.title("🔒 Servidor Arcade Python")
    
    # Pestañas para elegir entre Iniciar Sesión o Registrarse
    pestana_login, pestana_registro = st.tabs(["🔑 Iniciar Sesión", "📝 Crear Cuenta Nueva"])
    
    with pestana_login:
        usuario_input = st.text_input("Usuario:", key="log_user")
        password_input = st.text_input("Contraseña:", type="password", key="log_pass")
        
        if st.button("Ingresar al Juego"):
            datos_user = db.verificar_usuario(usuario_input, password_input)
            if datos_user:
                st.session_state.autenticado = True
                st.session_state.usuario = datos_user['username']
                st.session_state.coins = datos_user['monedas']
                st.session_state.nivel_guardado = datos_user['nivel_actual']
                
                # Ajustar el menú inicial según su progreso real guardado
                if st.session_state.nivel_guardado == 0:
                    st.session_state.menu_actual = "📋 Ganar Monedas (Entrevista)"
                elif st.session_state.nivel_guardado == 1:
                    st.session_state.menu_actual = "🎯 Jugar: Nivel 1 (Hola Mundo)"
                elif st.session_state.nivel_guardado == 2:
                    st.session_state.menu_actual = "⚡ Jugar: Nivel 2 (Variables)"
                else:
                    st.session_state.menu_actual = "🧮 Jugar: Nivel 3 (Matemáticas)"
                    
                st.success("¡Acceso concedido!")
                st.rerun()
            else:
                st.error("❌ Datos incorrectos.")
                
    with pestana_registro:
        nuevo_usuario = st.text_input("Elige un nombre de usuario:", key="reg_user")
        nueva_password = st.text_input("Elige una contraseña:", type="password", key="reg_pass")
        
        if st.button("Registrarme"):
            if nuevo_usuario.strip() == "" or nueva_password.strip() == "":
                st.error("❌ Los campos no pueden estar vacíos.")
            else:
                exito = db.registrar_usuario_db(nuevo_usuario, nueva_password)
                if exito:
                    st.success("🎉 ¡Cuenta creada con éxito! Ya puedes ir a la pestaña 'Iniciar Sesión'.")
                else:
                    st.error("❌ El nombre de usuario ya está ocupado. Intenta con otro.")

# --- PANTALLA DEL JUEGO ACTIVO ---
else:
    st.sidebar.title("🎮 Panel de Control")
    st.sidebar.write(f"🧑‍💻 Agente: **{st.session_state.usuario}**")
    st.sidebar.markdown(f"## 🪙 Monedas: **{st.session_state.coins}**")
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
        
    st.sidebar.write("---")

    # --- SISTEMA DE CANDADOS Y BLOQUEO ---
    progreso = st.session_state.nivel_guardado
    
    opciones_menu = ["📋 Ganar Monedas (Entrevista)"]
    
    # Bloqueo visual: Si su nivel guardado es menor, le muestra un candado
    opciones_menu.append("🎯 Jugar: Nivel 1 (Hola Mundo)" if progreso >= 1 else "🔒 Nivel 1 (Bloqueo)")
    opciones_menu.append("⚡ Jugar: Nivel 2 (Variables)" if progreso >= 2 else "🔒 Nivel 2 (Bloqueo)")
    opciones_menu.append("🧮 Jugar: Nivel 3 (Matemáticas)" if progreso >= 3 else "🔒 Nivel 3 (Bloqueo)")

    # Selector del menú usando la memoria global para los saltos automáticos
    st.session_state.menu_actual = st.sidebar.radio(
        "Navegación:", 
        opciones_menu, 
        index=opciones_menu.index(st.session_state.menu_actual) if st.session_state.menu_actual in opciones_menu else 0
    )

    st.title("🚀 Aprende Python - Modo Arcade")

    # Controlar que no intente entrar de forma tramposa a niveles bloqueados
    if "🔒" in st.session_state.menu_actual:
        st.warning("🚧 Este nivel está bloqueado. Debes completar los desafíos anteriores primero.")
    elif st.session_state.menu_actual == "📋 Ganar Monedas (Entrevista)":
        mostrar_encuesta()
    elif st.session_state.menu_actual == "🎯 Jugar: Nivel 1 (Hola Mundo)":
        nivel1.mostrar_nivel()
    elif st.session_state.menu_actual == "⚡ Jugar: Nivel 2 (Variables)":
        nivel2.mostrar_nivel()
    elif st.session_state.menu_actual == "🧮 Jugar: Nivel 3 (Matemáticas)":
        nivel3.mostrar_nivel()
