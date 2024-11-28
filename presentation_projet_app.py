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
   
   st.write("nouveau data set en supprimant la colone des gaz")
   if st.button(" nouveau dataset"):
      try:
         data = data.drop(['Production gaz renouvelable (GWh)'], axis = 1)
         cols = list(data.columns)
         cols
         data =data.rename(columns={cols[1]:"Regions", cols[2]:"Code_Regions", cols[3]:"Hydraulique_(GWh)", cols[4]:"Bioenergies_(GWh)",
                                    cols[5]:"Eolien_(GWh)", cols[6]:"Solaire_(GWh)", cols[7]:"Electrique_(GWh)",
                                    cols[8]:"Total_(GWh)", cols[9]:"Geo_shape", cols[10]:"Geo_point"})
         st.subheader("Nouveau Tableau des données")
         st.dataframe(data)
         
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
    st.write("présentation de graphique")
    

elif page == "Conclusion":
    st.header("Pour conclure")
    st.write("...")


