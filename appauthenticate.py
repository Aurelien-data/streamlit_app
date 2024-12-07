import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
from PIL import Image

# ETAPE 1
# création de l'instance d'authentification
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
   'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

# ETAPE 2
# Utiliser la méthode login pour afficher le formulaire de connexion (username & password) et vérifier les informations d'identification de l'utilisateur
authenticator.login()

# 2. Importer le module, créer le menu et récupérer la valeur sélectionnée
with st.sidebar:
    st.write('Bienvenue Utilisateur')
    selection = option_menu(
            menu_title= 'Menu',
            options= ['Accueil', 'Photos'],
            icons= ['house', 'camera'],
            menu_icon= 'cast'
                    )
    authenticator.logout("Déconnexion")
    

# Gérer l'accès en fonction des informations renseignées
def accueil():

    if st.session_state["authentication_status"]:
        accueil()
        st.image('Photos/photo_acceuil_batman.jpg', caption='blablabla')
            # Le bouton de déconnexion
    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")

    elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')


# 3. En fonction de l'option sélectionnée afficher le contenu correspondant dans votre application
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.header("Bienvenue sur le site dédié à Batman !")
    st.image('photo.jpg', width= 100)

if selection == "Photos":
    st.header("Album photo de Batman")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('photo1.jpg')
    with col2:
        st.image('photo2.jpg')
    with col3:
        st.image('photo3.png')