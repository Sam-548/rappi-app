import streamlit as st
from crecimiento import crecimientohistorico


st.set_page_config(
   page_title="Análisis de Rappi",
   page_icon="📊",
   layout="wide",
   initial_sidebar_state="expanded"
)

st.title("**Análisis de Rappi**")

st.sidebar.markdown("### Selecciona una sección:")

opciones_menu = [
   "Análisis de Crecimiento",
   "Recursos"
]

opcion_seleccionada = st.sidebar.selectbox(
   "",
   opciones_menu,
   index=0
)

st.markdown("---")

if opcion_seleccionada == "Análisis de Crecimiento":
   st.header("📊 Análisis de Crecimiento")
   crecimientohistorico()

elif opcion_seleccionada == "Recursos":
   st.header("📂 Recursos")
