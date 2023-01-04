import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
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


#- relacionar la edad c que prefieren hacer en el sup
st.subheader('Edad y preferencias')
sql6 = pd.DataFrame(run_query("SELECT edad,interes, COUNT(interes) FROM alumno GROUP BY edad, interes ORDER BY edad, interes;"))
sql6.columns = ['Edad','Interes', 'Cantidad']


chart2 = alt.Chart(sql6).mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
    ).encode(
        x='Edad:O',
        y='Cantidad:Q',
        color='Interes:N'
    )

st.altair_chart(chart2, use_container_width=True)

#st.table(sql6)