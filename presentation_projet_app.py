import streamlit as st
import pandas as pd

data = "https://github.com/mathildepmr/energie-renouvelable/blob/main/prod-region-annuelle-enr.csv"

page = st.sidebar.radio("Home page :", ["Introduction", "Problématique et data set", "Code python","Graphique", "Conclusion"])

if page == "Introduction":
   st.title('Projet Python') 
   st.markdown('''Mathilde Paumier, Antoni Riedberger, Nour Karam''')
   st.image("image.jpg")

elif page == "Problématique et data set":
   st.header("Problématique et data set")
   st.subheader(":green[Étude de l'impact de La guerre en Ukraine sur la production d'énergie renouvelable en France ]")
   st.write("Nous nous concentrerons sur les énergies renouvelables autre que le gaz à savoir l'éolien, l'hydraulique,le solaire et les bioénergies")
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
   boutinfo = st.button("Informations", use_container_width=True)
   if boutinfo:
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
 
   st.write("sélection de l'année 2022 et affichage de ses informations")
   st.image("image10.png")
   st.subheader(" ", divider="gray")

   st.write("statistique de l'année 2022")
   st.image("image11.png")
   st.write("Les représentations graphiques de ces statistiques se trouve sur l'onglet Graphique")
   st.subheader(" ", divider="gray")
   

elif page == "Graphique":
    st.header("Représentation Statistique")
    st.write("Statistique de la production d'énergies renouvelables pour l'année 2022")
    st.write("sélectionner un couple de variable pour plus de lisibilité, ici la production d'énergie d'origine éolien et solaire")
    st.write("filtrer pour faire un tableau comparatif entre les différentes années")
    st.write(" grouper par année")
    st.subheader ("graphique comparatif de l'évolution des énergies renouvelables")
    st.subheader ("graphique comparatif de l'évolution des énergies renouvelables avant et pendant la guerre en Ukraine")

   
elif page == "Conclusion":
    st.header("Pour conclure")
    st.write("...")


