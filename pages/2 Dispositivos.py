import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Dipositivos', 
                   page_icon='📊', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)


#header_style = '''
#    <style>
#        th{
#            background-color: #e7dc3f;
#        }
#    </style>
#'''
#st.markdown(header_style, unsafe_allow_html=True)


#st.header('Indicadores de tu grupo')
    

@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
st.subheader('Dispositivos utilizados')
sql3 = pd.DataFrame(run_query("SELECT dispositivo, COUNT(dispositivo) FROM alumno GROUP BY dispositivo"))
sql3.columns = ['Dispositivo', 'Cantidad']
#st.table(sql3)


st.subheader(f'La distribución de dispositivos es la siguiente:')
sql33 = pd.DataFrame(run_query("SELECT dispositivo, COUNT(dispositivo) FROM alumno GROUP BY dispositivo"))
sql33.columns = ['Dispositivo','Cantidad']
graf = alt.Chart(sql33).mark_bar().encode(
    x='Dispositivo', y='Cantidad', color= 'Dispositivo', tooltip=['Dispositivo', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, theme=None, use_container_width=True)

st.subheader('Microfono / Camara')

sql8 = pd.DataFrame(run_query("SELECT mic, COUNT(mic) FROM alumno GROUP BY mic;"))
sql8.columns = ['Microfono','Cantidad']
st.table(sql8)

base = alt.Chart(sql8).encode(
        theta=alt.Theta("Cantidad:Q", stack=True), color=alt.Color("Microfono:N", legend=None)
    )

pie = base.mark_arc(outerRadius=150)
text = base.mark_text(radius=180, size=12).encode(text="Microfono:N")

charte = pie + text

st.altair_chart(charte, use_container_width=True)

sql9 = pd.DataFrame(run_query("SELECT cam, COUNT(cam) FROM alumno GROUP BY cam;"))
sql9.columns = ['Camara','Cantidad']
st.table(sql9)

base2 = alt.Chart(sql9).encode(
        theta=alt.Theta("Cantidad:Q", stack=True), color=alt.Color("Camara:N", legend=None)
    )

pie2 = base2.mark_arc(outerRadius=150)
text2 = base2.mark_text(radius=180, size=12).encode(text="Camara:N")

chart2 = pie2 + text2

st.altair_chart(chart2, use_container_width=True)