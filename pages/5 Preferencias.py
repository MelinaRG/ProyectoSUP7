import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Preferencias', 
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


st.header('Indicadores de tu grupo')
    

@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- metrica con lo que preferirían hacer en el sup
st.subheader('Temas más elegidos para el SUP')
sql5 = pd.DataFrame(run_query("SELECT interes, COUNT(interes) as tot FROM alumno GROUP BY interes ORDER BY tot DESC"))
sql5.columns = ['Interés','Cantidad']
#st.table(sql5)


st.subheader(f'La distribución de preferencias es la siguiente:')
graf = alt.Chart(sql5).mark_bar().encode(
    x='Interés', y='Cantidad', color= 'Interés', tooltip=['Interés', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, theme=None, use_container_width=True)