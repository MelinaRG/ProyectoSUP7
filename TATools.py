import streamlit as st

st.set_page_config(page_title='Inicio', 
                   page_icon='🚀', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)

st.title('TA Tools :rocket:')

st.header('Esta app proporciona herramientas e información útil para TAs.')

st.subheader('En el menú a tu izquierda puedes acceder a distintas herramientas:')

st.subheader('**Mi Grupo**')
st.markdown("""
    En esta sección podrás ver el nombre de los integrantes
    de tu grupo, junto con sus direcciones de mail y
    usuarios de GIT.
""")

st.subheader('**Estadísticas**')
st.markdown("""
    Aquí puedes revisar la asistencia de tu grupo, también
    conocer cuáles son los temas de preferencia para habalar
    y si hay algún comentario o duda que responder.
""")

st.subheader('**Juegos**')
st.markdown("""
    Una de las actividades más entretenidas y que generan
    más distención en el grupo es jugar. Hemos armado una
    lista de páginas con alternativas para el entretenimiento.
""")
