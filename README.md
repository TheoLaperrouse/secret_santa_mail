# Secret Santa Mail

## Utilisation

1. Définir les différents participants et leur adresse mail dans user_infos.json
2. Définir les paires à exclure dans is_valid_pairs
2. Définir l'adresse mail utilisé pour envoyer les mails (MAIL dans .env)
3. Récupération JSON OAuth Google API
    1. Créer une application sur la console Google
    2. Activer l'API gmail
    3. Mettre en place l'OAuth
    4. Créer un client OAuth
    5. Récupérer le JSON et le mettre dans credentials.json

Lancer ensuite le programme pour envoyer un email à tous les participants pour qu'il découvre à qui offrir un cadeau : 
```bash
python3 secret_santa_mail.py
```