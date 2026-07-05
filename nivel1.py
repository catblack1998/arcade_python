import streamlit as st

def mostrar_nivel():
    st.subheader("🎯 Nivel 1: El Hechizo de Entrada")
    
    # Explicación
    st.markdown("""
    ### 📖 LA EXPLICACIÓN:
    En Python, usamos el comando `print()` para mostrar texto en la pantalla.
    
    **Ejemplo real:**
    ```python
    print("Hola Mundo")
    ```
    
    ⚠️ **REGLAS IMPORTANTES:**
    1. Todo debe ir en minúsculas: `print`
    2. El texto debe ir estrictamente entre comillas `" "`
    3. No olvides abrir y cerrar los paréntesis `( )`
    """)
    
    st.write("---")
    st.markdown("**TU DESAFÍO:** Escribe el código exacto para mostrar en pantalla el texto: *Hola Mundo*")
    
    # Entrada de código
    user_code = st.text_input("Escribe tu código de Python aquí:", placeholder="print(...)")
    
    # Botón para verificar
    if st.button("🚀 Lanzar Código (Cuesta 1 Moneda)"):
        # Validación de monedas disponibles
        if st.session_state.coins <= 0:
            st.error("💀 GAME OVER: Te quedaste sin monedas. ¡Debes ir a la pestaña de la encuesta a trabajar por más!")
            return
            
        # Descontar moneda por el intento
        st.session_state.coins -= 1
        
        # Comprobar respuesta
        correct_answer = 'print("Hola Mundo")'
        if user_code.strip() == correct_answer:
            st.success("🎉 ¡EXCELENTE! Has invocado tu primer código con éxito. ¡Nivel Completado!")
        else:
            if st.session_state.coins > 0:
                st.error(f"❌ Código incorrecto. ¡Revisa las comillas o paréntesis e intenta otra vez!")
            else:
                st.error("💀 GAME OVER: Gastaste tu última moneda. ¡Ve a la encuesta a recuperar fondos!")
        
        # Forzar recarga para actualizar el marcador de monedas de arriba
        st.rerun()
