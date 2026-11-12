import os
import streamlit as st
 
LOGO = "descarga.htm"  # guarda el logo en la misma carpeta que app.py
 
# ---------- BARRA LATERAL ----------
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")
 
if os.path.exists(LOGO):
    st.sidebar.image(LOGO)
else:
    st.sidebar.warning(f"No se encontró {LOGO}")
 
st.sidebar.button("Haz clic pero en la barra lateral")
 
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write("Escribiste en la barra:", texto_barra)
 
# ---------- ÁREA PRINCIPAL ----------
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")
 
if os.path.exists(LOGO):
    st.image(LOGO)
else:
    st.warning(f"No se encontró {LOGO}")
 
st.button("Haz clic")
 
texto = st.text_input("Escribe algo:")
st.write("Escribiste:", texto)
