import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
from scripts.db_postgres import conn

st.set_page_config(page_title='TA Tools - Nacionalidad', 
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
            color: #FFF
            background-color: #2B2B2B;
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


#- cant de alumnos por nacionalidad (barras)
st.subheader('Nacionalidades')
sql2 = pd.DataFrame(run_query("SELECT pais, COUNT(id_alumno) as Tot FROM alumno GROUP BY pais ORDER BY Tot DESC"))
sql2.columns = ['País','Cantidad']
#st.table(sql2)


st.subheader(f'La distribución de nacionalidades es la siguiente:')
graf = alt.Chart(sql2).mark_bar().encode(
    x='País', y='Cantidad', color= 'País', tooltip=['País', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, theme=None, use_container_width=True)