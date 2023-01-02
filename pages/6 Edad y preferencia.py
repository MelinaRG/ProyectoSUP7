import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Edad c/ Preferencia', 
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


#- relacionar la edad c que prefieren hacer en el sup
st.subheader('Edad y preferencias')
sql6 = pd.DataFrame(run_query("SELECT nombre,apellido,edad,interes FROM alumno ORDER BY edad"))
sql6.columns = ['Nombre','Apellido','Edad','Interés']
st.table(sql6)