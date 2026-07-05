import streamlit as st

def mostrar_nivel():
    st.subheader("🎯 Nivel 2: Las Cajas Mágicas (Variables)")
    
    # Explicación
    st.markdown("""
    ### 📖 LA EXPLICACIÓN:
    En programación, una **Variable** es como una caja con una etiqueta. Adentro de la caja puedes guardar textos, números o trucos.
    
    Para crear una variable, escribes su nombre, pones el signo igual `=` y luego lo que quieres guardar.
    
    **Ejemplo real:**
    ```python
    personaje = "Enmanuel"
    print(personaje)
    ```
    *Aquí creamos la caja llamada `personaje`, guardamos el texto `"Enmanuel"` adentro, y luego la mostramos en la pantalla.*
    
    ⚠️ **REGLAS IMPORTANTES:**
    1. Los nombres de las variables no llevan comillas.
    2. No uses espacios en el nombre de la caja (usa guion bajo si necesitas espacio, ej: `mi_nombre`).
    """)
    
    st.write("---")
    st.markdown("**TU DESAFÍO:** Crea una variable llamada `mascota` y guárdale el nombre `Firulais`. ¡No olvides las comillas para el nombre!")
    
    # Entrada de código
    user_code = st.text_input("Escribe tu código aquí:", placeholder="mascota = ...")
    
    # Botón para verificar
    if st.button("🚀 Lanzar Código (Cuesta 1 Moneda)"):
        if st.session_state.coins <= 0:
            st.error("💀 GAME OVER: Te quedaste sin monedas. ¡Ve a la encuesta a trabajar por más!")
            return
            
        st.session_state.coins -= 1
        
        # Validación (quitamos espacios de más para ayudarlo)
        clean_code = user_code.replace(" ", "")
        correct_answer_1 = 'mascota="Firulais"'
        correct_answer_2 = "mascota='Firulais'"
        
        if clean_code == correct_answer_1 or clean_code == correct_answer_2:
            st.success("🎉 ¡BRUTAL! Has guardado con éxito a Firulais en tu variable. ¡Eres un programador oficial!")
        else:
            if st.session_state.coins > 0:
                st.error("❌ Algo falló en la caja. Revisa que se llame `mascota`, tenga el `=` y el texto esté entre comillas.")
            else:
                st.error("💀 GAME OVER: Gastaste tu última moneda. ¡Ve a la encuesta a recuperar fondos!")
        
        st.rerun()
