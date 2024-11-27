import streamlit as st
import pandas as pd



st.title('Projet Python') 
st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
st.header("Problématique:") 
st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
st.subheader(" ", divider="gray")
st.subheader("Présentation du dataset")

page = st.sidebar.radio("Naviguer entre les pages :", ["Accueil", "Page 1", "Page 2"])

if page == "Accueil":
    st.header("Bienvenue sur la page d'accueil !")
    st.write("Cette application contient plusieurs pages. Utilisez le menu pour naviguer.")


elif page == "Page 1":
    st.header("Page 1 : Visualisation")
    st.write("Ajoutez ici votre contenu pour la première page.")
    # Exemple de graphique
    st.line_chart([1, 2, 3, 4, 5])


elif page == "Page 2":
    st.header("Page 2 : Analyse")
    st.write("Ajoutez ici votre contenu pour la deuxième page.")
    # Exemple de formulaire
    user_input = st.text_input("Entrez quelque chose :")
    if user_input:
        st.write(f"Vous avez entré : {user_input}")

