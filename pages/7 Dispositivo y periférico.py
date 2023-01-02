import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt
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
    

@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos
st.subheader('Microfono / Camara')
#sql7 = pd.DataFrame(run_query("SELECT nombre,apellido,dispositivo,mic,cam FROM alumno"))
#sql7.columns = ['Nombre','Apellido','Micrófono','Cámara','Periférico']
#st.table(sql7)

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