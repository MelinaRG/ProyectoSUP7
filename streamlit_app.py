# streamlit_app.py

import streamlit as st
import psycopg2


row1_1, row2_1 = st.columns((3,3))
with row1_1:
    st.title('Dashboard Proyecto SUP07')

with row2_1:
    st.text('Indicadores de la cohorte')
    
# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from Usuario;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")