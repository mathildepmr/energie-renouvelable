import streamlit as st
import pandas as pd


st.title('Projet Python') #page 1
st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
st.header("Problématique:") 
st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")


st.subheader(" ", divider="gray")
st.subheader("Présentation du dataset")

def page2():
    st.title("Code python")

pg = st.navigation([
    st.Page("page1.py", title="Introduction", icon="📝"),
    st.Page(page2, title="Code python", icon=":material/favorite:"),
])
pg.run()


