import streamlit as st
import db

def mostrar_nivel():
    st.subheader("🧮 Nivel 3: La Súper Calculadora")
    
    st.markdown("""
    ### 📖 LA EXPLICACIÓN:
    Python es genial con las matemáticas. Puedes sumar `+`, restar `-`, multiplicar `*` y dividir `/` números de forma directa.
    
    **Ejemplo real:**
    ```python
    resultado = 5 + 10
    print(resultado)
    ```
    *Esto guardará un 15 dentro de la variable.*
    """)
    
    st.write("---")
    st.markdown("**TU DESAFÍO:** Crea una variable llamada `resta` y guarda el resultado de restar **20 menos 7** (usa el operador `-`).")
    
    user_code = st.text_input("Escribe tu código aquí:", placeholder="resta = ...")
    
    if st.button("🚀 Lanzar Código (Cuesta 1 Moneda)"):
        if st.session_state.coins <= 0:
            st.error("💀 GAME OVER: Te quedaste sin monedas.")
            return
            
        st.session_state.coins -= 1
        clean_code = user_code.replace(" ", "")
        
        if clean_code == "resta=20-7":
            # Fin del juego actual
            st.success("🏆 ¡INCREÍBLE! Has terminado todos los niveles disponibles. ¡Eres oficialmente un programador Python! 🥳")
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, 3)
        else:
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, st.session_state.nivel_guardado)
            st.error("❌ La operación no es correcta. Recuerda: `resta = 20 - 7`")
        st.rerun()
