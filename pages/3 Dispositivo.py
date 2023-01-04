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


header_style = '''
    <style>
        th{
            background-color: #e7dc3f;
        }
    </style>
'''
st.markdown(header_style, unsafe_allow_html=True)


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