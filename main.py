import requests
import time
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env.local ou .env
if os.path.exists('.env.local'):
    load_dotenv('.env.local')
    print("Chargement de .env.local")
else:
    # Charger le fichier .env par défaut
    load_dotenv()
    print("Chargement de .env")

# Vos clés d'API LinkedIn et NewsAPI
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTH_URL = os.getenv('AUTH_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = os.getenv('NEWS_API_URL')
LINKEDIN_PROFILE_URL = os.getenv('LINKEDIN_PROFILE_URL')
LINKEDIN_IMAGE_UPLOAD_URL = os.getenv('LINKEDIN_IMAGE_UPLOAD_URL')
LINKEDIN_SHARE_POST = os.getenv('LINKEDIN_SHARE_POST')

# Liste pour suivre les articles déjà publiés
articles_publies = []


# Fonction pour obtenir l'access token LinkedIn via OAuth2
def obtenir_access_token(client_id, client_secret, redirect_uri, auth_code):
    try:
        data = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret
        }
        response = requests.post(TOKEN_URL, data=data)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        response_data = response.json()
        return response_data.get('access_token')
    except Exception as e:
        print(f"Erreur lors de la récupération du token : {e}")
        return None


# Fonction pour obtenir l'URN de l'utilisateur LinkedIn
def obtenir_urn_utilisateur(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(LINKEDIN_PROFILE_URL, headers=headers)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    profile_data = response.json()
    return profile_data.get('sub')


# Fonction pour extraire des articles technologiques
def extraire_articles_tech():
    try:
        params = {
            'apiKey': NEWS_API_KEY,
            'category': 'technology',
            'language': 'en',
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        articles_filtres = [article for article in articles if
                            "[Removed]" not in article['title'] and "removed" not in article['title'].lower()]
        return articles_filtres
    except Exception as e:
        print(f"Erreur lors de l'extraction des articles : {e}")
        return []


# Fonction pour obtenir l'URL d'upload de l'image sur LinkedIn
def obtenir_url_upload_image(access_token, urn_utilisateur):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "registerUploadRequest": {
                "owner": f"urn:li:person:{urn_utilisateur}",
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"]
            }
        }
        response = requests.post(LINKEDIN_IMAGE_UPLOAD_URL, headers=headers, json=data)
        response.raise_for_status()
        upload_info = response.json()
        upload_url = \
        upload_info['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
            'uploadUrl']
        asset = upload_info['value']['asset']
        return upload_url, asset
    except Exception as e:
        print(f"Erreur lors de l'obtention de l'URL d'upload de l'image : {e}")
        return None, None


# Fonction pour télécharger l'image
def telecharger_image(upload_url, image_url):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        headers = {
            'Content-Type': 'image/jpeg'
        }
        upload_response = requests.put(upload_url, headers=headers, data=image_response.content)
        upload_response.raise_for_status()
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image : {e}")
        return False


# Fonction pour créer un post LinkedIn
def creer_post_linkedin(titre, lien, image_asset):
    return {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": f"Découvrez cet article intéressant en technologie : {titre}\n{lien}"
            },
            "shareMediaCategory": "IMAGE",
            "media": [{
                "status": "READY",
                "description": {
                    "text": f"Découvrez cet article intéressant en technologie : {titre}"
                },
                "media": image_asset,
                "title": {
                    "text": titre
                }
            }]
        }
    }


# Fonction pour publier un post sur LinkedIn
def publier_sur_linkedin(post, access_token, urn_utilisateur):
    url = LINKEDIN_SHARE_POST
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "author": f"urn:li:person:{urn_utilisateur}",
        "lifecycleState": "PUBLISHED",
        "specificContent": post,
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Post publié avec succès sur LinkedIn.")
    else:
        print(f"Erreur lors de la publication : {response.status_code} - {response.text}")


# Fonction pour afficher un compte à rebours
def afficher_compte_a_rebours(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\rProchain post dans : {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTemps écoulé, publication d'un nouvel article ! ")


# Intervalle de publication (en secondes)
intervalle = 60 * 5  # 5 minutes pour tester (changer en 86400 pour 24 heures)

# Étape 1 : Obtenir l'URL d'autorisation OAuth2
auth_params = {
    'response_type': 'code',
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'scope': 'openid profile email w_member_social'
}
auth_url = requests.Request('GET', AUTH_URL, params=auth_params).prepare().url
print(f"Visitez cette URL pour autoriser l'application : {auth_url}")

# Étape 2 : Entrer le code d'autorisation obtenu via l'URL
authorization_code = input("Collez le code d'autorisation ici : ")

# Étape 3 : Obtenir un access token à partir du code d'autorisation
access_token = obtenir_access_token(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, authorization_code)

if access_token:
    # Obtenir l'URN de l'utilisateur LinkedIn
    urn_utilisateur = obtenir_urn_utilisateur(access_token)
    if urn_utilisateur:
        while True:
            articles = extraire_articles_tech()
            for article in articles:
                if article['url'] in articles_publies:
                    continue  # Ignorer les articles déjà publiés

                titre = article['title']
                lien = article['url']
                image_url = article.get('urlToImage')

                # Obtenir l'URL d'upload de l'image
                upload_url, image_asset = obtenir_url_upload_image(access_token, urn_utilisateur)
                if upload_url and image_asset and image_url:
                    if telecharger_image(upload_url, image_url):
                        # Créer le post LinkedIn
                        post = creer_post_linkedin(titre, lien, image_asset)
                        # Publier le post sur LinkedIn
                        publier_sur_linkedin(post, access_token, urn_utilisateur)
                        # Ajouter l'URL de l'article à la liste des articles publiés
                        articles_publies.append(article['url'])
                    else:
                        print("Erreur lors du téléchargement de l'image.")
                else:
                    print("Erreur lors de l'obtention de l'URL d'upload de l'image.")

                afficher_compte_a_rebours(intervalle)
    else:
        print("Impossible d'obtenir l'URN utilisateur.")
else:
    print("Impossible d'obtenir un access token.")