import streamlit as st
import pandas as pd

data = "https://github.com/mathildepmr/energie-renouvelable/blob/main/prod-region-annuelle-enr.csv"

page = st.sidebar.radio("Sommaire :", ["Introduction", "Problématique et data set", "Code python","Graphique", "Conclusion"])

if page == "Introduction":
   st.title('Projet Python') 
   st.markdown('''Mathilde Paumier, Antony Riedberger, Nour Karam''')
   st.image("image.jpg")

elif page == "Problématique et data set":
   st.header("Problématique et data set")
   st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France en fonction des années ]")
   st.subheader(" ", divider="gray")
   
   csv_url = "https://raw.githubusercontent.com/mathildepmr/energie-renouvelable/main/prod-region-annuelle-enr.csv"
   st.title("dataset : Énergies Renouvelables")
   def load_csv(url):
      return pd.read_csv(url, sep=";")
   if st.button("dataset"):
      try:
         data = load_csv(csv_url)
         st.success("Données chargées avec succès !")
         st.subheader("Tableau des données")
         st.dataframe(data)
      except Exception as e:
         st.error(f"Erreur lors du chargement des données : {e}")
   
   
elif page == "Code python":
   st.header("Code Python")
   st.write("visualisation des différentes informations du dataset")
   st.image("image2.png")
   st.subheader(" ", divider="gray")

   st.write("Supression de la colone de gaz et remplacement des valeurs manquantes")
   st.write("Colones renommées pour faciliter la lecture")
   st.image("image8.png")
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
   st.image("image5.png")
   st.subheader(" ", divider="gray")
 
   st.write("sélection de l'année 2023 et affichage de ces informations")
   st.image("image7.png")
   st.subheader(" ", divider="gray")

   st.write("statistique de l'année 2023")
   st.image("image6.png")
   st.write("Les représentations graphiques de ces statistiques se trouve sur l'onglet Graphique")
   st.subheader(" ", divider="gray")
   

elif page == "Graphique":
    st.header("Graphique")
    st.write("présentation de graphique")
    

elif page == "Conclusion":
    st.header("Pour conclure")
    st.write("...")


