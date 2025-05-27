import streamlit as st
from crecimiento import crecimientohistorico
from crecimiento import liquidez_solvencia


st.set_page_config(
   page_title="Análisis de Rappi",
   page_icon="📊",
   layout="wide",
   initial_sidebar_state="expanded"
)

st.title("**Análisis de Rappi**")

st.sidebar.markdown("### Selecciona una sección:")

opciones_menu = [
   "Historia",
   "Análisis de Crecimiento",
   "Liquidez y Solvencia",
   "Conclusiones",
   "Recursos"
]

opcion_seleccionada = st.sidebar.selectbox(
   "",
   opciones_menu,
   index=0
)

st.markdown("---")

if opcion_seleccionada == "Historia":
   st.markdown('<h1 style="color: indianred;">- 🗃️ Historia de la empresa', unsafe_allow_html=True)
   st.markdown("""
   ### Resumen Breve de Rappi

   Rappi empezó en **2015** en Bogotá para facilitar compras de supermercado online. Su trayectoria incluye una rápida expansión a múltiples servicios de entrega, convertirse en el primer unicornio tecnológico colombiano (**2018**) tras inversiones clave como la de Y Combinator (**2016**) y especialmente la de Softbank (\$1 mil millones en **2019**). Tres eventos cruciales fueron: **(1)** alcanzar el estatus de unicornio, **(2)** la inversión masiva de Softbank, y **(3)** su exitosa diversificación de servicios (Rappi Turbo, Rappi Card) durante la pandemia, lo que impulsó su continuo crecimiento y una reciente adquisición en IA (**2024**).
   """)

elif opcion_seleccionada == "Análisis de Crecimiento":
   st.header("📊 Análisis de Crecimiento")
   crecimientohistorico()

elif opcion_seleccionada == " Liquidez y Solvencia":
   liquidez_solvencia()

elif opcion_seleccionada == "Conclusiones":
   st.markdown('<h1 style="color: yellow;">- 📚 Conclusiones', unsafe_allow_html=True)
   st.markdown("""
   ### Análisis de Problemáticas y Soluciones Propuestas

   * **Problemática:** Baja rentabilidad operativa sostenida y utilidad neta negativa.
      * **Solución:** Revisar costos fijos y administrativos, automatizar procesos, redirigir inversión a mercados dominantes (Colombia y Perú), y ampliar líneas de ingresos con productos financieros o suscripciones de alto margen.

   * **Problemática:** Disminución significativa en la liquidez operativa y días de reservas de caja.
      * **Solución:** Establecer una política de caja mínima estratégica, renegociar plazos de pago con proveedores, e implementar un modelo de presupuestación por escenarios.

   * **Problemática:** Alta dependencia del financiamiento externo.
      * **Solución:** Fortalecer la transparencia financiera con inversionistas, establecer alianzas estratégicas con actores del sector retail o financiero, y evaluar una eventual salida a bolsa (IPO).

   * **Problemática:** Gestión ineficiente del capital de trabajo y uso intensivo de cuentas por pagar.
      * **Solución:** Implementar un sistema de gestión de capital de trabajo en tiempo real, establecer incentivos para el pronto pago de comercios aliados, y digitalizar procesos logísticos.
   """)

elif opcion_seleccionada == "Recursos":
   st.header("📂 Recursos")
