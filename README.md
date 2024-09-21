# 🚀 Bot de Publication Automatique sur LinkedIn

Ce projet est un **bot de publication automatique sur LinkedIn** qui extrait des articles technologiques en temps réel à partir de l'API de NewsAPI.org, et les publie automatiquement sur votre profil LinkedIn. Le bot est conçu pour gérer les autorisations OAuth2, télécharger des images associées aux articles, et préparer des posts de manière dynamique, tout en évitant les duplications.

---

## 📚 Fonctionnalités

- Extraction d'articles technologiques en temps réel via l'API [NewsAPI.org](https://newsapi.org/).
- Publication automatique d'articles sur votre **profil LinkedIn**.
- Gestion des images associées aux articles.
- Evite les duplications d'articles déjà publiés.
- Intervalle de publication configurable.

---

## 🛠️ Installation

### Pré-requis

- **Python 3.7+**
- Un compte [LinkedIn Developer](https://www.linkedin.com/developers/)
- Clés API pour [NewsAPI.org](https://newsapi.org/)

### Étapes d'installation

1. Clonez ce dépôt GitHub sur votre machine locale :

   ```bash
   git clone https://github.com/Nassim-Abid/Bot-de-publication-automatique-sur-LinkedIn.git
   cd votre-repo
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Créez un fichier ```.env``` à la racine de votre projet avec les informations suivantes :
   ```
   # Fichier .env
   CLIENT_ID=VotreClientID
   CLIENT_SECRET=VotreClientSecret
   REDIRECT_URI=http://localhost:8000/code
   NEWS_API_KEY=VotreNewsAPIKey
   ```
4. Si vous avez un fichier de configuration local, créez un fichier .env.local pour écraser les valeurs de .env si nécessaire.
   ```
   # Fichier .env.local
   CLIENT_ID=VotreClientIDLocal
   CLIENT_SECRET=VotreClientSecretLocal
   ```
5. Exécutez le bot :
   ```bash
   python main.py
   ```
## ⚙️ Utilisation
### Configuration OAuth2
Pour publier sur LinkedIn, vous devez configurer OAuth2 pour obtenir un token d'accès.

Rendez-vous sur l'URL d'autorisation générée dans le terminal.
Connectez-vous avec votre compte LinkedIn et copiez le code d'autorisation.
Collez ce code dans le terminal lorsque le programme vous le demande.
Le bot se charge ensuite de récupérer automatiquement les articles et de les publier à intervalles réguliers.

### Exemples
Si vous souhaitez tester avec des intervalles courts (ex : toutes les 5 minutes), modifiez l'intervalle dans le code :
   ```
   intervalle = 60 * 5  # 5 minutes
   ```
Pour un intervalle quotidien (ex : toutes les 24 heures) :
   ```
   intervalle = 60 * 60 * 24  # 24 heures
   ```
## 🐛 Dépannage
### Problème courant : Erreur 403 lors de la publication
- Vérifiez que vous avez bien les permissions nécessaires via l'API LinkedIn.
- Assurez-vous que votre jeton d'accès n'a pas expiré.
- Confirmez que vous utilisez la **bonne URN** pour publier sur un profil personnel et non une page organisationnelle.

## 🤝 Contribution
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, suivez les étapes suivantes :

1. **Fork** le projet.
2. Créez une nouvelle branche : git checkout -b feature-nouvelle-fonctionnalite.
3. Faites vos modifications.
4. Soumettez une **Pull Request.**

## 📄 License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

## 📧 Contact
Si vous avez des questions ou souhaitez collaborer, n'hésitez pas à me contacter à l'adresse : [nassimabiddz@gmail.com](mailto:nassimabiddz@gmail.com).
