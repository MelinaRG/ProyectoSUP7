import streamlit as st
import pandas as pd

st.write ("""
# Hola chiquis
## Analizando a *Fede*

""")

a = st.slider('Que tan crack es fede? (1-50 es re cobani, 50-100 es un crack)' , 0, 100, 25)
