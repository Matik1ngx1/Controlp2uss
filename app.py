import os
 
import streamlit as st
 
LOGO = "descarga.jpg"  # debe estar en la misma carpeta que app.py
 
 
def mostrar_logo(contenedor):
    """Muestra el logo; si falta o está dañado, avisa en vez de romper la app."""
    if not os.path.exists(LOGO):
        contenedor.warning(f"No se encontró {LOGO}")
        return
    try:
        contenedor.image(LOGO)
    except Exception:
        contenedor.warning(f"{LOGO} no es una imagen válida. Vuelve a guardarla como PNG y súbela de nuevo.")
 
 
# ---------- BARRA LATERAL ----------
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")
 
mostrar_logo(st.sidebar)
 
st.sidebar.button("Haz clic pero en la barra lateral")
 
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write("Escribiste en la barra:", texto_barra)
 
# ---------- ÁREA PRINCIPAL ----------
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")
 
mostrar_logo(st)
 
st.button("Haz clic")
 
texto = st.text_input("Escribe algo:")
st.write("Escribiste:", texto)
