import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Dispositivos c/ periféricos', 
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
    

# Initialize connection.
# Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
#    return psycopg2.connect(**st.secrets["postgres"])

#conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos
st.subheader('Dispositivos y conexión')
sql7 = pd.DataFrame(run_query("SELECT nombre,apellido,dispositivo,mic,cam FROM alumno"))
sql7.columns = ['Nombre','Apellido','Micrófono','Cámara','Periférico']
st.table(sql7)