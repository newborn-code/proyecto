import pandas as pd
import streamlit as st 
import plotly.express as px

st.header('PROYECTO: HISTOGRAMA')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.checkbox ('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

#Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión
disp_button = st.checkbox ('Crear un grafico de dispersion')

if disp_button:
        st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')

        fig2 = px.scatter(car_data, x="odometer")

        st.plotly_chart(fig2, use_container_width=True)

#if disp_button:
        
 #       st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')


#print('PRUEBA')    
#print(car_data)
