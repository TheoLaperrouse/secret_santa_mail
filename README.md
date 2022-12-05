# Secret Santa Mail

## Mise en place

### Récupération Mot de passe d'application Google

1. Allez sur gérer mon compte google
2. Sous "Se connecter à Google", vérifiez que la "vérification en deux étapes" est activée pour le compte.
3. Toujours sous "Connexion à Google", sélectionnez "Mots de passe de l'application".
4. Sélectionnez l'application "Mail" et l'appareil "Autre (nom personnalisé)" et donnez-lui un nom.
5. Copiez le mot de passe de l'application, il se trouve dans un encart jaune et ressemble à ceci : "XXXX XXXX XXXX XXXX XXXX", coller le ensuite dans la variable EMAIL_PASSWORD du .env et renseigner l'adresse

### Récupération de la libraire python-dotenv

Installer les dépendances à partir du requirements.txt :
```bash
pip3 install -r requirements.txt
```

## Utilisation

Définir les différents participants et leur adresse mail dans user_infos.json

Lancer ensuite le programme pour envoyer un email à tous les participants pour qu'il découvre à qui offrir un cadeau : 
```bash
python3 secret_santa_mail.py
```