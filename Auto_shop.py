import streamlit as st
import pandas as pd


# Titre
st.markdown("<h1 style='text-align: center; color: black;'>MY DATA AUTO SHOP</h1>", unsafe_allow_html=True)

st.markdown("""
Téléchargez facilement les données sur les voitures, scooters, équipements disponibles sur Expat-Dakar, 
récupérées automatiquement via le web scraping avec **BeautifulSoup** ou **Web Scraper**.
""")

# Initialisation de la session
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fonction pour revenir à l'accueil
def retour():
    st.session_state.page = "home"

# Fonction d'affichage avec bouton
def load_(dataframe, title, key, source):
    st.markdown("""
        <style>
        div.stButton { text-align: center; margin-top: 15px; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.6em 1em;
            font-size: 16px;
            border: none;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.page == "home":
        if st.button(title, key=key):
            st.session_state.page = key
            st.session_state.data = dataframe
            st.session_state.source = source
            st.session_state.title = title

# Si l'utilisateur a cliqué sur un bouton
if st.session_state.page != "home":
    st.markdown(f"{st.session_state.title}")
    st.markdown(f" Source scraping :`{st.session_state.source}`")
    st.success(f"{st.session_state.data.shape[0]} lignes × {st.session_state.data.shape[1]} colonnes")
    st.dataframe(st.session_state.data)
    st.button("🔙 Retour", on_click=retour)

# Page d'accueil avec les boutons
if st.session_state.page == "home":
    st.markdown("## Données extraites avec BeautifulSoup")

    try:
        load_(pd.read_csv('data_code_nettoye/equis .csv'), 'equis', '1', 'BeautifulSoup')
        load_(pd.read_csv('data_code_nettoye/scooters.csv'), 'Scooters ', '2', 'BeautifulSoup')
        load_(pd.read_csv('data_code_nettoye/voitures.csv'), 'Voitures', '3', 'BeautifulSoup')
    except FileNotFoundError as e:
        st.error(f"Erreur de chargement : {e}")

    st.markdown("## Données extraites avec Web Scraper")

    try:
        load_(pd.read_csv('data/piece_web_scarper.csv'), 'equipement', '4', 'Web Scraper')
        load_(pd.read_csv('data/scooter_web_scarper.csv'), 'Scooters', '5', 'Web Scraper')
        load_(pd.read_csv('data/voiture_web_scraper.csv'), 'Voitures', '6', 'Web Scraper')
    except FileNotFoundError as e:
        st.error(f"Erreur de chargement : {e}")

    st.markdown("## 📝 Formulaire d'évaluation")

    # Ajout du formulaire KoBoToolbox (iframe intégré)
    st.markdown("""
    <iframe src="https://ee.kobotoolbox.org/i/XNpaW4VM" width="100%" height="600" frameborder="0"></iframe>
    """, unsafe_allow_html=True)