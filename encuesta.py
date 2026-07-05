import streamlit as st
import db

def mostrar_encuesta():
    st.subheader("📋 Encuesta de Responsabilidad")
    st.write("Responde con la verdad para reclamar tus monedas del día:")
    
    # Preguntas de responsabilidad
    p1 = st.checkbox("¿Ordenaste tu cuarto hoy?")
    p2 = st.checkbox("¿Hiciste tus deberes escolares o tareas asignadas?")
    p3 = st.checkbox("¿Leíste o practicaste algo productivo hoy?")
    
    if st.button("🧧 Reclamar Monedas"):
        if p1 and p2 and p3:
            st.session_state.coins = 3
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, 1)
            st.success("¡Excelente! Has demostrado ser responsable. ¡Recibes 3 monedas! Go, go, go! 🪙🪙🪙")
            # Forzar recarga para actualizar el marcador
            st.rerun()
        else:
            st.error("❌ Para ganar monedas debes cumplir con todas tus responsabilidades. ¡Inténtalo de nuevo!")
