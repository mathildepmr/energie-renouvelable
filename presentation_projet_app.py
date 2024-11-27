import streamlit as st
import pandas as pd



st.title('Projet Python') #page 1
st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
st.header("Problématique:") 
st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
st.subheader(" ", divider="gray")
st.subheader("Présentation du dataset")

def page_2():
    st.title("Code Python ")

pg = st.navigation([st.Page("page_1.py"), st.Page(page_2)])
pg.run()

