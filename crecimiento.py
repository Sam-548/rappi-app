import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def crecimientohistorico():
   """Función que contiene todo el contenido del análisis de crecimiento"""
  
   # Crecimiento historico________________
   st.markdown('<h1 style="color: indianred;">- Crecimiento histórico</h1>', unsafe_allow_html=True)
  
   st.markdown("#### En 2018 alcanzó el estatus de unicornio, con una valoración de 1.000 millones de dólares.")
   st.markdown("#### Para febrero de 2025, su valor estimado de mercado alcanzó los 5.4 mil millones de dólares, lo que representa un incremento del 440% en siete años. Este aumento equivale a una tasa de crecimiento anual compuesta (CAGR) aproximada del 27.4%. ")
   st.markdown("#### Rappi reportó $1.300 millones de ingresos en 2024, reflejando una tasa de crecimiento interanual del 51.95%")
   st.markdown("#### Aunque su valorización de mercado ha sido volátil, el crecimiento de sus ingresos ha sido constante, impulsado por su expansión y su adaptación a las condiciones cambiantes del mercado.")


   col1, col2 = st.columns(2)
   años = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
   ingresos = [77, 198, 395, 250, 387, 553, 703]

   with col1:
       fig_ingresos = go.Figure()
       fig_ingresos.add_trace(go.Scatter(x=años, y=ingresos, mode='lines+markers', name='Ingresos', line=dict(color='indianred')))
       fig_ingresos.update_layout(
           title='Ingresos Anuales Estimados de Rappi (2018–2024)',
           xaxis_title='Año',
           yaxis_title='Ingresos (millones de USD)',
           template='plotly_white'
       )
       st.plotly_chart(fig_ingresos, use_container_width=True)


   with col2:
       valoracion = [1000, 3500, 3800, 4300, 5250, 5300, 5400]
       fig_valoracion = go.Figure()
       fig_valoracion.add_trace(go.Scatter(x=años, y=valoracion, mode='lines+markers', name='Valoración', line=dict(color='indianred')))
       fig_valoracion.update_layout(
           title='Valoración de Mercado Estimada de Rappi (2018–2024)',
           xaxis_title='Año',
           yaxis_title='Valoración (millones de USD)',
           template='plotly_white'
       )
       st.plotly_chart(fig_valoracion, use_container_width=True)

   # Comparación con otras empresas ______________________

   años = ["Sept 2018", "May 2019", "Abr 2021", "Jul 2021", "May 2024"]
   valoracion = [1.0, 3.5, 4.3, 5.2, 5.4]  
   fig = go.Figure(data=[
    go.Bar(
        x=años,
        y=valoracion,
        text=[f"{v:.1f}" for v in valoracion],
        textposition='auto',
        marker_color='indianred'
    )
        ])
    
   fig.update_layout(
    title='Valor de mercado de Rappi de 2018 a 2024 (en miles de millones de USD)',
    xaxis_title='Fecha',
    yaxis_title='Valor de mercado (miles de millones USD)',
    yaxis=dict(range=[0, 6]),
    template='plotly_white'
     )
   
   st.plotly_chart(fig)

   st.markdown('<h1 style="color: indianred;">- Comparación con competidores</h1>', unsafe_allow_html=True)


   st.markdown("""#### Rappi ha mantenido una de las tasas de expansión más agresivas. Pero al analizar el mercado concluimos que sus mayores competidores en Latinoamérica serían *UberEats y iFood*.""")


   st.markdown('<h1 style="color: mediumseagreen;">🇧🇷🍽️ iFood</h1>', unsafe_allow_html=True)


   col1, col2 = st.columns(2)


   años = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
   ingresos_rappi = [77, 198, 395, 250, 387, 553, 703] 
   ingresos_ifood = [117, 148, 315, 624, 991, 1400, 1089]
   valoracion_rappi = [1000, 3500, 3800, 4300, 5250, 5300, 5400]
   valoracion_ifood = [1000, 1800, 2750, 4500, 5400, 5600, None]


   with col1:
       st.subheader("Ingresos Anuales Estimados (en millones de USD)")
       fig_ingresos = go.Figure()
       fig_ingresos.add_trace(go.Scatter(x=años, y=ingresos_rappi, mode='lines+markers', name='Rappi', line=dict(color='indianred')))
       fig_ingresos.add_trace(go.Scatter(x=años, y=ingresos_ifood, mode='lines+markers', name='iFood', line=dict(color='mediumseagreen')))
       fig_ingresos.update_layout(xaxis_title='Año', yaxis_title='Ingresos (millones de USD)')
       st.plotly_chart(fig_ingresos)


   with col2:
       st.subheader("Valoración de Mercado Estimada (en millones de USD)")
       fig_valoracion = go.Figure()
       fig_valoracion.add_trace(go.Scatter(x=años, y=valoracion_rappi, mode='lines+markers', name='Rappi', line=dict(color='indianred')))
       fig_valoracion.add_trace(go.Scatter(x=años, y=valoracion_ifood, mode='lines+markers', name='iFood', line=dict(color='mediumseagreen', dash='dash')))
       fig_valoracion.update_layout(xaxis_title='Año', yaxis_title='Valoración (millones de USD)')
       st.plotly_chart(fig_valoracion)

   

   st.markdown("""* #### 💰 ***Ingresos***: iFood ha mostrado un crecimiento más acelerado en ingresos, especialmente a partir de 2022, superando a Rappi en este aspecto.""")
   st.markdown("""* #### 📈 ***Valoración de Mercado***: Ambas empresas han incrementado su valoración de mercado de manera constante, con iFood alcanzando una valoración ligeramente superior a la de Rappi en 2025.""")
   st.markdown("""* #### 🌎 ***Expansión***: Mientras iFood ha consolidado su liderazgo en Brasil, Rappi ha logrado posicionarse como líder en Colombia, México y otros mercados emergentes.""")


   st.markdown('<h1 style="color: mediumseagreen;">🚗🍔 UberEats</h1>', unsafe_allow_html=True)


   st.markdown("""#### Uber Eats ha reducido sus operaciones en varios países de LATAM, mientras que Rappi ha diversificado sus líneas de negocio.""")


   data = {'Año': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
   'Rappi': [77, 198, 395, 250, 387, 553, 703],
   'Uber Eats LATAM': [1200, 1500, 1800, 2100, 2500, 2800, 3000]}


   df = pd.DataFrame(data)


   col1, col2 = st.columns(2)


   with col1:
       st.markdown("""### Crecimiento Histórico de Ingresos (2018-2024)""")
       fig = go.Figure()
       fig.add_trace(go.Scatter(x=df['Año'], y=df['Rappi'], mode='lines+markers', name='Rappi', line=dict(color='indianred')))
       fig.add_trace(go.Scatter(x=df['Año'], y=df['Uber Eats LATAM'], mode='lines+markers', name='Uber Eats LATAM', line=dict(color='mediumseagreen')))
       fig.update_layout(
           xaxis_title='Año',
           yaxis_title='Ingresos (millones de USD)',
           hovermode='x unified'
       )
       st.plotly_chart(fig)
  
   with col2:
       st.markdown("### Comparación de Ingresos en 2022")
       ingresos_2022 = {
           'Empresa': ['Rappi', 'Uber Eats LATAM'],
           'Ingresos': [387, 522]
       }
       fig_bar = go.Figure()
       fig_bar.add_trace(go.Bar(x=['Rappi'], y=[381], marker_color='indianred', name='Rappi'))
       fig_bar.add_trace(go.Bar(x=['Uber Eats LATAM'], y=[522], marker_color='mediumseagreen', name='Uber Eats LATAM'))
       fig_bar.update_layout(
       xaxis_title='Empresa',
       yaxis_title='Ingresos (millones de USD)'
       )
       st.plotly_chart(fig_bar)


   st.markdown('<h2 style="color: mediumseagreen;">1. 📈 Rappi muestra un crecimiento más acelerado en términos relativos</h2>', unsafe_allow_html=True)
   st.markdown("* #### Rappi pasó de 220M en 2018 a 1.300M en 2024, lo que representa un crecimiento de +491% en 7 años.")
   st.markdown("* #### Uber Eats LATAM pasó de 1.200M a 3.000M, un crecimiento de +150% en el mismo período.")
   st.markdown("* #### Esto sugiere que, aunque Uber Eats genera más ingresos absolutos, Rappi crece a un ritmo más acelerado proporcionalmente.")


   st.markdown('<h2 style="color: mediumseagreen;">2. 🌎 Rappi ha ganado terreno competitivo en LATAM</h2>', unsafe_allow_html=True)
   st.markdown("* #### A pesar de contar con menos recursos globales que Uber, Rappi ha logrado capturar una porción creciente del mercado LATAM. Con enfoque en países clave como Colombia, México y Perú.")


   st.markdown('<h2 style="color: mediumseagreen;">3. 💸 Uber Eats mantiene la ventaja en volumen de ingresos</h2>', unsafe_allow_html=True)
   st.markdown("* #### En 2024, Uber Eats LATAM genera más del doble de ingresos que Rappi (3B vs 1.3B).")
   st.markdown("* #### Esto muestra que, aunque Rappi crece rápido, aún no alcanza la escala regional de Uber Eats.")


   st.markdown('<h2 style="color: mediumseagreen;">4. 📊 Las gráficas indican una tendencia', unsafe_allow_html=True)
   st.markdown("* #### Uber Eats en LATAM muestra un crecimiento más plano a partir de 2022, pasando de 2.5B a 3.0B en dos años (solo +20%). sto puede reflejar una maduración del mercado para UberEats.")
   st.markdown("* #### Las curvas de crecimiento muestran que la brecha entre ambos se está reduciendo lentamente, pero Uber Eats aún domina en ingresos brutos.")
   st.markdown("* #### Esta tendencia se puede mantener si Rappi asegura su crecimiento de +50% anual.")


   # Tasa de crecimiento sostenible


   st.markdown('<h1 style="color: indianred;">- Tasa de crecimiento sostenible</h1>', unsafe_allow_html=True)
   #EXCEL
   st.dataframe(df)
   st.markdown("* ### Al ser una empresa de base tecnológica en expansión y sin dividendos, se estima que Rappi reinvierte el 100% de sus utilidades, por lo que su TCS estaría directamente relacionada con su rentabilidad sobre el capital (ROE).")
   st.markdown("* ### Lo que maximiza la tasa de crecimiento sostenible, siempre que haya utilidad y ROE positivo.")
   st.markdown("* ### En empresas como Rappi, el payout es 0%, ya que no reparten dividendos y priorizan el crecimiento e inversión interna.")
   