import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Edades', 
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
# Display a static table


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


#- edad promedio de alumnos, c la min y max
sql1 = run_query("SELECT ROUND(AVG(edad),0) FROM alumno")
sql11 = run_query("SELECT MIN(edad) , MAX(edad) FROM alumno")  
col1, col2, col3 = st.columns(3)
col1.metric(label="Menor", value=int(sql11[0][0]), delta=None)
col2.metric(label="Edad promedio", value=int(sql1[0][0]), delta=None)
col3.metric(label="Mayor", value=int(sql11[0][1]), delta=None)


st.subheader('Edades de los alumnos')
sql111 = pd.DataFrame(run_query("SELECT nombre,apellido,edad FROM alumno ORDER BY edad"))
sql111.columns = ['Nombre','Apellido','Edad']
#st.table(sql111)