import streamlit as st
from crecimiento import crecimientohistorico
from crecimiento import liquidez_solvencia
import numpy as np
import pandas as pd


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

elif opcion_seleccionada == "Liquidez y Solvencia":
   st.markdown('<h1 style="color: cyan;">- 💧 Análisis de Liquidez y Solvencia</h1>', unsafe_allow_html=True)

   st.subheader("Tabla 1: ESTIMADORES LIQUIDEZ (Primer Grupo)")

   data1 = {
        'ESTIMADORES': ['Razón corriente', 'Prueba defensiva', 'Cash holding', 'Días de reserva de cash', 'FCO a deuda CP', 'Nivel de apalancamiento'],
        '2023': [1.296979, '14%', '10%', 29.68, -0.193928, '87,73%'],
        '2022': [1.207449, '22%', '18%', 57.97, -0.886851, '91,99%'],
        '2021': [1.061922, '46%', '42%', 119.62, -0.283551, '104,15%'],
        '2020': [1.170396, '26%', '22%', 25.75, -1.362316, '105,52%'],
        '2019': [1.400623, '54%', '36%', 44.86, -2.165623, '102,82%']
    }
   df1 = pd.DataFrame(data1)
   st.dataframe(df1.set_index('ESTIMADORES'))

   st.subheader("Tabla 2: ESTIMADORES INSOLVENCIA (Primer Grupo)")
   data2 = {
        'ESTIMADORES': ["Z''-score de Altman", 'Modelo Zmijewsky'],
        '2023': [-0.72, 0.36], 
        '2022': [-2.28, 0.16],
        '2021': [-3.86, 0.01],
        '2020': [-4.90, 0.15],
        '2019': [-7.24, 0.44] 
    }
   df2 = pd.DataFrame(data2)
   st.dataframe(df2.set_index('ESTIMADORES'))


   st.subheader("Tabla 3: ESTIMADORES LIQUIDEZ (Segundo Grupo)")
   data3 = {
        'ESTIMADORES': ['Razón corriente', 'Prueba defensiva', 'Cash holding', 'Días de reserva de cash', 'FCO a deuda CP', 'Nivel de apalancamiento'],
        '2023': [1.543, '67%', '19,7%', 27.38, 0.08319, '31,19%'],
        '2022': [2.509, '107%', '16,5%', 21.52, -0.487972509, '27,34%'],
        '2021': [2.817, '180%', '28,7%', 41.61, -0.54308094, '26,70%'],
        '2020': [2.605, '82%', '14,7%', 28.67, 0.040898263, '151,69%'],
        '2019': [4.311, '94%', '9,4%', 64.11, 0.100033493, '143,31%']
    }
   df3 = pd.DataFrame(data3)
   st.dataframe(df3.set_index('ESTIMADORES'))

   st.subheader("Tabla 4: ESTIMADORES INSOLVENCIA (Segundo Grupo)")
   data4 = {
        'ESTIMADORES': ["Z''-score de Altman", 'Ratio deuda/activos'],
        '2023': [-3.76, 0.16], # Assuming '-' means NaN
        '2022': [0.99, 0.16],
        '2021': [1.26, 0.16],
        '2020': [-3.18, 1.39],
        '2019': [-0.21, 1.34] # Corrected: was 0.21 based on first table, looks like 3.18 in second
    }
   df4 = pd.DataFrame(data4)
   st.dataframe(df4.set_index('ESTIMADORES'))

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
