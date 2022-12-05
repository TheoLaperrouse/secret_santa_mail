import random
import json
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv


def send_mail(sender,receiver,email_users):
    """Send an email to the receiver

    Args:
        sender (str): name of the sender
        receiver (str): name of the receiver
        email_users (dict): email associated to name
    """
    _ = load_dotenv()
    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")
    msg = EmailMessage()
    msg['Subject'] = f"Bonjour {sender}, vous devez offrir un cadeau à {receiver}"
    msg['To'] = email_users[receiver]
    msg.set_content(f"Bonjour {sender}, vous devez offrir un cadeau à {receiver}.\nBon Secret Santa")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.starttls()
    smtpserver.login(email_address, email_password)
    smtpserver.send_message(msg)



if __name__ == "__main__":
    infos = open('user_infos.json', encoding='utf-8')
    user_infos = json.load(infos)
    pairs = []
    names = list(user_infos.keys())
    random.shuffle(names)
    names_shifted = names[1:] + names[:1]
    for index, name in enumerate(names):
        pairs.append([name, names_shifted[index]])
    for pair in pairs: 
        send_mail(pair[0], pair[1], user_infos)

