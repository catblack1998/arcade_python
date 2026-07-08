import streamlit as st
import db

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
    
    ⚠️ **REGLAS IMPORTANTES:**
    1. Los nombres de las variables no llevan comillas.
    2. No uses espacios en el nombre de la caja.
    """)
    
    st.write("---")
    st.markdown("**TU DESAFÍO:** Crea una variable llamada `mascota` y guárdale el nombre `Firulais`. ¡No olvides las comillas para el nombre!")
    
    # Entrada de código
    user_code = st.text_input("Escribe tu código aquí:", placeholder="mascota = ...")
    
    # Botón para verificar
    if st.button("🚀 Lanzar Código (Cuesta 1 Moneda)"):
        if st.session_state.coins <= 0:
            st.error("💀 GAME OVER: Te quedaste sin monedas. ¡Debes ir a la pestaña de la encuesta a trabajar por más!")
            return
            
        st.session_state.coins -= 1
        
        # Validación limpia (eliminando espacios para evitar falsos errores)
        clean_code = user_code.replace(" ", "")
        correct_answer_1 = 'mascota="Firulais"'
        correct_answer_2 = "mascota='Firulais'"
        
        if clean_code == correct_answer_1 or clean_code == correct_answer_2:
            # 1. Subir el nivel guardado a 3 en la memoria global
            st.session_state.nivel_guardado = 3
            
            # 2. Guardar el nuevo nivel y las monedas actuales en Clever Cloud
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, 3)
            
            st.success("🎉 ¡BRUTAL! Has completado el Nivel 2. ¡Teletransportándote al Nivel 3...!")
            
            # 3. ORDEN MÁGICA: Cambiar la navegación automática al Nivel 3 y reiniciar la pantalla
            st.session_state.menu_actual = "🧮 Jugar: Nivel 3 (Matemáticas)"
            st.rerun()
        else:
            # Si se equivoca, guardamos la resta de la moneda en la base de datos
            db.actualizar_progreso_db(st.session_state.usuario, st.session_state.coins, st.session_state.nivel_guardado)
            
            if st.session_state.coins > 0:
                st.error("❌ Algo falló en tu caja. Revisa que se llame `mascota`, tenga el `=` y el texto esté entre comillas.")
            else:
                st.error("💀 GAME OVER: Gastaste tu última moneda. ¡Ve a la encuesta a recuperar fondos!")
            st.rerun()
