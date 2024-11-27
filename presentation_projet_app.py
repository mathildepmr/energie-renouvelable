import streamlit as st
import pandas as pd
from sklearn.datasets import 

page = st.sidebar.radio("Naviguer entre les pages :", ["Introduction", "Problématique et data set", "Code python","Graphique", "Conclusion"])

if page == "Introduction":
   st.title('Projet Python') 
   st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
   st.image("image.jpg")

elif page == "Problématique et data set":
   st.header("Problématique et data set")
   st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
   st.subheader(" ", divider="gray")
   st.subheader("Présentation du dataset")

   
elif page == "Code python":
    st.header("Code Python")
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

