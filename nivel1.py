import streamlit as st
import db

def mostrar_nivel():
    st.subheader("🎯 Nivel 1: El Hechizo de Entrada")
    
    st.markdown("""
    ### 📖 LA EXPLICACIÓN:
    En Python, usamos el comando `print()` para mostrar texto en la pantalla.
    
    ```python
    print("Hola Mundo")
    ```
    """)
    
    st.markdown("**TU DESAFÍO:** Escribe el código exacto para mostrar en pantalla el texto: *Hola Mundo*")
    user_code = st.text_input("Escribe tu código de Python aquí:", placeholder="print(...)")
    
    if st.button("🚀 Lanzar Código (Cuesta 1 Moneda)"):
        if st.session_state.coins <= 0:
            st.error("💀 GAME OVER: Te quedaste sin monedas. ¡Vuelve a hacer la entrevista por fondos!")
            return
            
        st.session_state.coins -= 1
        correct_answer = 'print("Hola Mundo")'
        
        if user_code.strip() == correct_answer:
            # Subir el nivel guardado en la base de datos a Nivel 2
            st.session_state.nivel_guardado = 2
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, 2)
            
            st.success("🎉 ¡EXCELENTE! Has completado el Nivel 1. ¡Teletransportándote al Nivel 2...!")
            
            # Salto automático al Nivel 2
            st.session_state.menu_actual = "⚡ Jugar: Nivel 2 (Variables)"
            st.rerun()
        else:
            # Guardamos la resta de la moneda en la DB
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, st.session_state.nivel_guardado)
            if st.session_state.coins > 0:
                st.error("❌ Código incorrecto. ¡Inténtalo otra vez!")
            else:
                st.error("💀 GAME OVER: Gastaste tu última moneda.")
            st.rerun()
