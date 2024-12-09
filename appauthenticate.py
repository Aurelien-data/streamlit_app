import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# ETAPE 1
# création de l'instance d'authentification
# je déclare les données de compte des utlisateurs et de l'admmin
lesDonneesDesComptes = {
                        'usernames':
                        {
                        'utilisateur':
                         {
                        'name': 'utilisateur',                  # informations pour un seul utilisateur
                        'password': 'utilisateurMDP',           # informations pour un seul utilisateur
                        'email': 'utilisateur@gmail.com',       # informations pour un seul utilisateur
                        'failed_login_attemps': 0,              # informations pour un seul utilisateur
                        'logged_in': False,                     # informations pour un seul utilisateur
                        'role': 'utilisateur'                   # informations pour un seul utilisateur
                        },
                        'root': 
                        {
                        'name': 'root',                         # informations pour l'admin
                        'password': 'rootMDP',                  # informations pour l'admin
                        'email': 'admin@gmail.com',             # informations pour l'admin
                        'failed_login_attemps': 0,              # informations pour l'admin
                        'logged_in': False,                     # informations pour l'admin
                        'role': 'administrateur'                # informations pour l'admin
                        }
                    }
                }

# je stocke dans une variable la class Authenticate, qui contient les données de compte
authenticator = Authenticate(
    lesDonneesDesComptes,                                       # Les données des comptes
    "cookie name",                                              # Le nom du cookie, un str quelconque
    "cookie key",                                               # La clé du cookie, un str quelconque
    30,                                                         # Le nombre de jours avant que le cookie expire 
)

# ETAPE 2
# Utiliser la méthode login pour afficher le formulaire de connexion (username & password) et vérifier les informations d'identification de l'utilisateur
authenticator.login()

# A PARTIR DE MAINTENANT, ON CREER LA DTRUCTURE ET LE CONTENU DU SITE
# 2. Importer le module, créer le menu et récupérer la valeur sélectionnée



# Gérer l'accès en fonction des informations renseignées
def accueil():
    st.title('Bienvenu sur le Bat site')
def accueil_photos():
    st.title("Bienvenu dans l'album photo de Batman")

if st.session_state["authentication_status"]:

    with st.sidebar:
        st.write('Bienvenue Utilisateur')
        selection = option_menu(
            menu_title= 'Menu',
            options= ['Accueil', 'Photos'],
            icons= ['house', 'camera'],
            menu_icon= 'cast'
                    )
    
        authenticator.logout("Déconnexion")


    if selection == "Accueil":
        accueil()
        st.image('photo.jpg')

    elif selection == "Photos":
        accueil_photos()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image('photo1.jpg')
            st.write('il est pas content')

        with col2:
            st.image('photo2.jpg')
            st.write('derrière lui ça brule')
            
        with col3:
            st.image('photo3.png')
            st.write("j'espère que ce logo a bercé ton enfance")

        # Le bouton de déconnexion
    if st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")

    if st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')