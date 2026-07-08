import streamlit as st
import db

def mostrar_encuesta():
    st.subheader("📋 Entrevista Inicial de Programación")
    st.write("Responde estas preguntas para desbloquear tus herramientas y ganar tus primeras monedas:")
    
    p1 = st.text_input("1. ¿Tienes alguna experiencia previa en programación?", placeholder="Ej: Ninguna, o he visto videos...")
    p2 = st.text_input("2. ¿Qué te gustaría crear o hacer después de aprender a programar?", placeholder="Ej: Crear videojuegos, páginas web...")
    p3 = st.text_input("3. Con tus propias palabras, ¿sabes o te imaginas qué es Python?", placeholder="Ej: Un lenguaje para computadoras...")
    
    st.write("---")
    
    if st.button("🧧 Enviar Entrevista y Empezar Juego"):
        if p1.strip() == "" or p2.strip() == "" or p3.strip() == "":
            st.error("❌ Por favor, escribe algo en cada una de las respuestas antes de enviar.")
        else:
            # Otorgar monedas
            st.session_state.coins = 3
            # Guardamos progreso: nivel_actual pasa a ser 1 (Ya desbloqueó el nivel 1)
            st.session_state.nivel_guardado = 1
            
            db.actualizar_progreso_db(
                st.session_state.usuario, 
                st.session_state.coins, 
                1, 
                exp=p1, meta=p2, que_es=p3
            )
            
            st.success("🎉 ¡Felicidades! Has obtenido 3 monedas. ¡Cargando Nivel 1...!")
            
            # TRUCO MÁGICO: Cambiamos el menú actual y forzamos reinicio para saltar al Nivel 1 automáticamente
            st.session_state.menu_actual = "🎯 Jugar: Nivel 1 (Hola Mundo)"
            st.rerun()
