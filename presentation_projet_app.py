import streamlit as st
import pandas as pd

data = "https://github.com/mathildepmr/energie-renouvelable/blob/main/prod-region-annuelle-enr.csv"

page = st.sidebar.radio("Naviguer entre les pages :", ["Introduction", "Problématique et data set,icon="😃", "Code python","Graphique", "Conclusion"])

if page == "Introduction":
   st.title('Projet Python') 
   st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
   st.image("image.jpg")

elif page == "Problématique et data set,icon="😃":
   st.header("Problématique et data set")
   st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
   st.subheader(" ", divider="gray")
   st.subheader("Présentation du data set")
   
   
 
elif page == "Code python":
   st.header("Code Python")
   st.write("visualisation des différentes informations du dataset")
   st.image("image2.png")
   st.subheader(" ", divider="gray")
   
   st.write("nouveau data set en supprimant la colone des gaz")
   st.subheader(" ", divider="gray")
   
   st.write("conversion des Années et des Régions en str")

   boutannee = st.button("Année", use_container_width=True)
   if boutannee:
      st.image("image3.png")
      
   boutregion = st.button("Région", use_container_width=True)
   if boutregion:
      st.image("image4.png")
   else:
    st.write("Cliquez sur le bouton pour voir une image.")
         
   st.subheader(" ", divider="gray")
   
   st.write("Années en index")
   st.subheader(" ", divider="gray")
   
   st.write("sélection de l'année 2023 et affichage de ces informations")
   st.subheader(" ", divider="gray")
   

elif page == "Graphique":
    st.header("Graphique")
    st.write(" ")
    

elif page == "Conclusion":
    st.header("Pour conclure")
    st.write("Ajoutez ici votre contenu pour la deuxième page.")


