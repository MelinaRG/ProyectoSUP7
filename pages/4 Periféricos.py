import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Periféricos', 
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
            background-color: yellow;
        }
    </style>
'''
st.markdown(header_style, unsafe_allow_html=True)


st.header('Indicadores de tu grupo')
    

@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- cant de alumnos q poseen tanto mic como cam
st.subheader('Uso de cámara y/o micrófono')
sql4 = pd.DataFrame(run_query("SELECT mic, COUNT(mic) as Tot FROM alumno GROUP BY mic ORDER BY Tot DESC"))
sql4.columns = ['Micrófono','Cantidad']
st.table(sql4)


st.subheader(f'La distribución de periféricos es la siguiente:')
graf = alt.Chart(sql4).mark_bar().encode(
    x='Micrófono', y='Cantidad', color= 'Micrófono', tooltip=['Micrófono', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, use_container_width=True)


st.subheader('Uso de cámara y/o micrófono')
sql44 = pd.DataFrame(run_query("SELECT cam, COUNT(cam) as Tot FROM alumno GROUP BY cam ORDER BY Tot DESC"))
sql44.columns = ['Cámara','Cantidad']
st.table(sql44)


st.subheader(f'La distribución de periféricos es la siguiente:')
graf = alt.Chart(sql44).mark_bar().encode(
    x='Cámara', y='Cantidad', color= 'Cámara', tooltip=['Cámara', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, use_container_width=True)