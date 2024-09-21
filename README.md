# 🚀 Automatic Posting Bot on LinkedIn

This project is an automatic posting bot on LinkedIn that extracts real-time technology articles from the NewsAPI.org API and automatically posts them on your LinkedIn profile. The bot is designed to handle OAuth2 authorizations, download images associated with the articles, and prepare posts dynamically while avoiding duplications.

# 📚 Features
- Real-time extraction of technology articles via the [NewsAPI.org](https://newsapi.org/).
- Automatic posting of articles on your LinkedIn profile.
- Management of images associated with the articles.
- Avoids duplication of already published articles.
- Configurable posting interval.

---

# 🛠️ Installation 
## Prerequisites
- Python 3.7+
- A LinkedIn Developer account
- API keys for NewsAPI.org

## Installation Steps
1. Clone this GitHub repository to your local machine:
   ```
   git clone https://github.com/Nassim-Abid/Bot-de-Publication-Automatique-sur-LinkedIn.git
   cd Bot-de-Publication-Automatique-sur-LinkedIn
   ```
1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a .env file at the root of your project with the following information:
   ```
   .env file
   CLIENT_ID=YourClientID
   CLIENT_SECRET=YourClientSecret
   REDIRECT_URI=http://localhost:8000/code
   NEWS_API_KEY=YourNewsAPIKey
   ```
3. If you have a local configuration file, create a .env.local file to override the values in .env if necessary.
   ```
   .env.local file
   CLIENT_ID=YourLocalClientID
   CLIENT_SECRET=YourLocalClientSecret
   ```
4. Run the bot:
   ```bash
   python main.py
   ```
# ⚙️ UsageOAuth2 Configuration
To post on LinkedIn, you need to configure OAuth2 to obtain an access token.

1. Go to the authorization URL generated in the terminal.
2. Log in with your LinkedIn account and copy the authorization code.
3. Paste this code into the terminal when prompted by the program.
4. The bot will then automatically retrieve articles and post them at regular intervals. 
### Examples
If you want to test with short intervals (e.g., every 5 minutes), modify the interval in the code:
   ```
   interval = 60 * 5  # 5 minutes
   ```
For a daily interval (e.g., every 24 hours):
   ```
   interval = 60 * 60 * 24  # 24 hours
   ```
# 🐛 Troubleshooting 
### Common Issue: 403 Error When Posting
- Check that you have the necessary permissions via the LinkedIn API.
- Ensure your access token has not expired.
- Confirm you are using the correct URN to post on a personal profile and not an organizational page.
# 🤝 Contribution
Contributions are welcome! If you want to improve this project, follow these steps:
- **Fork** the project.
- Create a new branch: git checkout -b feature-new-feature.
- Make your changes.
- Submit a **Pull Request**.
# 📄 License
This project is licensed under the MIT License. See the LICENSE file for more information.
# 📧 Contact 
If you have any questions or want to collaborate, feel free to contact me at: [nassimabiddz@gmail.com](mailto:nassimabiddz@gmail.com).
Let me know if you need any further assistance!
