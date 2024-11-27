import streamlit as st
import pandas as pd


page = st.sidebar.radio("Naviguer entre les pages :", ["Accueil", "Page 1", "Page 2"])

if page == "Accueil":
   st.title('Projet Python') 
    st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
    st.header("Problématique:") 
    st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
    st.subheader(" ", divider="gray")
    st.subheader("Présentation du dataset")


elif page == "Code python":
    st.header("Page 1 : Visualisation")
    st.write("Ajoutez ici votre contenu pour la première page.")
    # Exemple de graphique
    st.line_chart([1, 2, 3, 4, 5])


elif page == "Graphique":
    st.header("Page 2 : Analyse")
    st.write("Ajoutez ici votre contenu pour la deuxième page.")
    # Exemple de formulaire
    user_input = st.text_input("Entrez quelque chose :")

elif page == "Conclusion":
    st.header("Page 2 : Analyse")
    st.write("Ajoutez ici votre contenu pour la deuxième page.")
    # Exemple de formulaire
    user_input = st.text_input("Entrez quelque chose :")
    if user_input:
        st.write(f"Vous avez entré : {user_input}")

