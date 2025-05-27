import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np

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
           title='Ingresos Anuales de Rappi (2018–2024)',
           xaxis_title='Año',
           yaxis_title='Ingresos (miles de millones)',
           template='plotly_white'
       )
       st.plotly_chart(fig_ingresos, use_container_width=True)


   with col2:
       valoracion = [1000, 3500, 3800, 4300, 5250, 5300, 5400]
       fig_valoracion = go.Figure()
       fig_valoracion.add_trace(go.Scatter(x=años, y=valoracion, mode='lines+markers', name='Valoración', line=dict(color='indianred')))
       fig_valoracion.update_layout(
           title='Valoración de Mercado de Rappi (2018–2024)',
           xaxis_title='Año',
           yaxis_title='Valoración (miles de millones)',
           template='plotly_white'
       )
       st.plotly_chart(fig_valoracion, use_container_width=True)


   col1, col2 = st.columns(2)

   with col1:
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
        title='Valor de Rappi (en miles de millones). Statista.',
        xaxis_title='Fecha',
        yaxis_title='Valor de mercado (miles de millones)',
        yaxis=dict(range=[0, 6]),
        template='plotly_white'
        )
    
    st.plotly_chart(fig)

    with col2:
        years = [2016, 2017, 2018, 2019, 2020, 2021]
        ingresos_equilibrio = [6.048918, 18.938456, 77.227243, 198.980406, 394.800098, 249.529876]
        utilidades = [-19.226306, -56.333228, -156.014697, -305.808851, -234.338238, -243.468088]
        
        fig_equilibrio = go.Figure()

        fig_equilibrio.add_trace(go.Scatter(
            x=years,
            y=ingresos_equilibrio,
            mode='lines+markers',
            name='Ingresos',
            line=dict(color='indianred'),
            marker=dict(color='indianred')
        ))

        fig_equilibrio.add_trace(go.Scatter(
            x=years,
            y=utilidades,
            mode='lines+markers',
            name='Utilidades netas',
            line=dict(color='orange'),
            marker=dict(color='orange')
        ))

        fig_equilibrio.add_hline(y=0, line_dash="dash", line_color="gray", line_width=1)

        fig_equilibrio.update_layout(
            title='Punto de Equilibrio (miles de millones). Supersociedades.',
            xaxis_title='Año',
            yaxis_title='Cifras (miles de pesos)',
            template='plotly_white',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        st.plotly_chart(fig_equilibrio, use_container_width=True)

   # Comparación de competidores

   st.markdown('<h1 style="color: indianred;">- Comparación con competidores</h1>', unsafe_allow_html=True)


   st.markdown("""#### Rappi ha mantenido una de las tasas de expansión más agresivas. Pero al analizar el mercado concluimos que sus mayores competidores en Latinoamérica serían *iFood, PedidosYa, DidiFood y Uber Eats*.""")

   # Gráfico 1

   data = {
    'Month': ['Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020',
              'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020', 'Dec 2020',
              'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021'],
    'iFood': [86, 81, 69, 71, 74, 73, 77, 87, 87, 88, 88, 87, 87, 88, 83, 80, 89, 83],
    'Rappi': [11, 14, 26, 23, 21, 20, 17, 10, 11, 11, 11, 11, 10, 9, 13, 15, 8, 13],
    'Uber Eats': [3, 5, 5, 6, 5, 7, 6, 3, 2, 1, 1, 2, 2, 3, 4, 5, 3, 4]
   }

   fig = go.Figure()

   fig.add_trace(go.Bar(
    name='iFood',
    x=data['Month'],
    y=data['iFood'],
    marker_color='#E31E24',
    text=[f'{val}%' for val in data['iFood']],
    textposition='inside',
    textfont=dict(color='white', size=12, family='Arial')
   ))

   fig.add_trace(go.Bar(
    name='Rappi',
    x=data['Month'],
    y=data['Rappi'],
    marker_color='#FF6B35',
    text=[f'{val}%' for val in data['Rappi']],
    textposition='inside',
    textfont=dict(color='white', size=12, family='Arial')
   ))

   fig.add_trace(go.Bar(
    name='Uber Eats',
    x=data['Month'],
    y=data['Uber Eats'],
    marker_color='#2B2B2B',
    text=[f'{val}%' for val in data['Uber Eats']],
    textposition='inside',
    textfont=dict(color='white', size=12, family='Arial')
    ))

   fig.update_layout(
    title={
        'text': 'Brazil Food Delivery Market Share<br><sub>% of Total Orders (USD)</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 28, 'color': 'white', 'family': 'Arial Bold'}
    },
    barmode='stack',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white', family='Arial'),
    height=600,
    margin=dict(l=50, r=50, t=100, b=100),
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=1.15,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(0,0,0,0)',
        font=dict(size=14)
    )
   )

   fig.update_xaxes(
    showgrid=False,
    showline=False,
    tickangle=45,
    tickfont=dict(size=12, color='white'),
    title=dict(text='', font=dict(size=14, color='white'))
   )

   fig.update_yaxes(
    showgrid=True,
    gridcolor='rgba(255,255,255,0.1)',
    showline=False,
    tickfont=dict(size=12, color='white'),
    title=dict(text='% of Total Orders (USD)', font=dict(size=14, color='white')),
    range=[0, 100]
   )

   st.plotly_chart(fig, use_container_width=True)

   # Gráfico 2 y 3
   col1, col2 = st.columns(2)
   
   with col1:
      año = 2023
      empresas = ['Rappi', 'iFood']
      ingresos = [553, 5525]
      colores_empresas = {'Rappi': 'indianred', 'iFood': 'mediumseagreen'}

      data = {'Empresa': empresas, 'Ingresos': ingresos}
      df = pd.DataFrame(data)
      colores_empresas = {'Rappi': 'indianred', 'iFood': 'mediumseagreen'}

      fig = px.bar(df, 
                    x='Empresa', 
                    y='Ingresos', 
                    title='Ingresos de iFood y Rappi en 2023',
                    labels={'Ingresos': 'Ingresos (miles de millones de pesos)'},
                    text_auto=True,
                    color='Empresa',
                    color_discrete_map=colores_empresas)
      
      fig.update_traces(textfont_color='white', textposition='auto')
      fig.update_layout(
            xaxis_title='Empresa',
            yaxis_title='Ingresos (miles de millones de pesos)',
            title_x=0.5,
            showlegend=False
        )
      
      st.plotly_chart(fig)

   with col2:
      st.image("https://images.prismic.io/sacra/6a95921c-b025-4a74-b326-0ce7ef670b22_image16.png?auto=compress,format")

   markdown_summary = """
    #### * **📌 Crecimiento continuo:** El mercado latinoamericano de delivery sigue expandiéndose, con potencial en ciudades secundarias y nuevas categorías como supermercados.
    #### * **📌 Dominio fragmentado por regiones:** No hay un líder único regional; iFood domina Brasil, mientras Rappi, PedidosYa y Didi Food compiten en otros mercados.
    #### * **📌 La rentabilidad es el gran reto:** A pesar del crecimiento, ser rentable es difícil, llevando a estrategias como diversificación (ej. "super-apps"), optimización logística y eficiencia.
    #### * **📌 Adaptación e innovación constantes:** El éxito requiere ajustarse a los consumidores, innovar en servicios (ej. entregas ultra rápidas) y gestionar desafíos operativos/regulatorios.
    #### * **📌 Consolidación y maduración:** Se espera que el mercado se consolide, beneficiando a empresas eficientes, diversificadas y con usuarios leales para lograr rentabilidad a largo plazo.
    """

   st.markdown(markdown_summary)

   # Tasa de crecimiento sostenible

   st.markdown('<h1 style="color: indianred;">- Tasa de crecimiento sostenible</h1>', unsafe_allow_html=True)
   data = {
    '2023': ['-$ 5.145,20', '-9%', '$ -', '-$ 0,09'],
    '2022': ['-$ 199.461,50', '-530%', '$ -', '$ 5,30'],
    '2021': ['-$ 243.468,09', '1446%', '$ -', '$ 14,46'],
    '2020': ['-$ 234.338,24', '2049%', '$ -', '$ 20,49'],
    '2019': ['-$ 305.808,85', '6461%', '$ -', '$ 64,61']
    }
   index_labels = ['Utilidad Neta', 'ROE', 'Payout', 'TCS']

   df = pd.DataFrame(data, index=index_labels)
   df.index.name = "Indicadores"

   def style_negative_currency(val):
    if isinstance(val, str) and val.startswith('-$'):
        return 'color: red;'
    return ''

   styled_df = df.style.applymap(style_negative_currency)\
                    .set_table_styles([
                        {'selector': 'th',
                         'props': [('font-weight', 'bold'),
                                   ('text-align', 'left'),
                                   ('border-style', 'solid'),
                                   ('border-width', '1px'),
                                   ('border-color', 'lightgrey')]},
                        {'selector': 'th.col_heading',
                         'props': [('text-align', 'right'),
                                   ('background-color', '#E8E8E8')]},
                        {'selector': 'th.index_name',
                         'props': [('background-color', '#E8E8E8')]},
                        {'selector': 'td',
                         'props': [('text-align', 'right'),
                                   ('border-style', 'solid'),
                                   ('border-width', '1px'),
                                   ('border-color', 'lightgrey')]}
                    ])

   st.dataframe(styled_df, use_container_width=True)
   st.markdown("* ### Al ser una empresa de base tecnológica en expansión y sin dividendos, se estima que Rappi reinvierte el 100% de sus utilidades, por lo que su TCS estaría directamente relacionada con su rentabilidad sobre el capital (ROE).")
   st.markdown("* ### Lo que maximiza la tasa de crecimiento sostenible, siempre que haya utilidad y ROE positivo.")
   st.markdown("* ### En empresas como Rappi, el payout es 0%, ya que no reparten dividendos y priorizan el crecimiento e inversión interna.")
   
   
# Indicadores de Liquidez

def liquidez_solvencia():
   
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
        '2023': [-0.72, 0.36], # Assuming '-' means NaN for numeric interpretation
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

   
    