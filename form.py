import streamlit as st
import sqlite3

conn = sqlite3.connect('data.csv', check_same_thread = False)
cur = conn.cursor()

def form():
    st.write('Datos para TAs')
    with st.form(key= 'Formulario de relevamiento'):
        Nombre =st.text_input('Ingrese su nombre: ')
        Edad = st.text_input('Ingrese su edad: ')
        Carrera = st.text_input('Ingrese la carrera: ')
        Cohorte = st.text_input('Ingrese su cohorte')
        submission = st.form_submit_button(label = 'Enviar')
        if submission == True:
            addData(Nombre, Edad, Carrera, Cohorte)

def addData(a,b,c,d):
    cur.execute("""CREATE TABLE IF NOT EXISTS clg_form(Nombre TEXT(50), Edad TEXT(10), Carrera TEXT(50), Cohorte TEXT(50))""")
    cur.execute("INSERT INTO clg_form VALUES (?,?,?,?)", (a,b,c,d))
    conn.commit()
    conn.close()
    st.success('Formulario enviado')

form()