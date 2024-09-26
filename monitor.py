import requests
import smtplib
from email.mime.text import MIMEText

# URL de mon portfolio à surveiller
URL = 'http://mahery-64.github.io/mahery-gv/'  

# Fonction de vérification de la disponibilité
def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Le site {url} est en ligne.")
            return True
        else:
            print(f"Erreur: Le site {url} a renvoyé un statut {response.status_code}.")
            return False
    except requests.ConnectionError:
        print(f"Erreur: Impossible de se connecter à {url}.")
        return False

# Fonction pour envoyer un email en cas de problème
def send_alert(email_content):
    # Configurer l'adresse et le mot de passe de l'expéditeur (à configurer selon le fournisseur d'email)
    sender_email = 'exemple@gmail.com'
    sender_password = 'test123'
    receiver_email = 'exemple@gmail.com'  

    # Configuration du message
    msg = MIMEText(email_content)
    msg['Subject'] = 'Alerte du Bot Monitoring: Problème détecté'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Connexion au serveur SMTP et envoi de l'email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

# Fonction principale de monitoring
def monitor():
    site_is_up = check_site(URL)
    if not site_is_up:
        send_alert(f"Le site {URL} est hors ligne ou rencontre des problèmes.")

# Exécuter le monitoring
if __name__ == '__main__':
    monitor()
