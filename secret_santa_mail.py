from __future__ import print_function
import os.path
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random
import json
import base64
from dotenv import load_dotenv

load_dotenv()
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def is_valid_pairs(pairs):
    if len(pairs) == 0:
        return False
    EXCLUDED_PAIRS = [
    ]
    return all(
        pair not in EXCLUDED_PAIRS and pair[::-1] not in EXCLUDED_PAIRS
        for pair in pairs
    )


def get_pairs():
    pairs = []
    names = list(user_infos.keys())
    random.shuffle(names)
    names_shifted = names[1:] + names[:1]
    for index, name in enumerate(names):
        pairs.append([name, names_shifted[index]])
    return pairs


def send_mail(sender, receiver, email_users, service):
    with open("template.html", "r", encoding="utf-8") as file:
        template_html = file.read()

    template_html = template_html.replace("{{ sender }}", sender).replace(
        "{{ receiver }}", receiver
    )

    msg = EmailMessage()
    msg[
        "Subject"
    ] = f"Père Noël Secret : découvrez de qui vous êtes le Père Noël secret"
    msg["To"] = email_users[receiver]
    msg.set_content(template_html, subtype="html")

    raw_message = base64.urlsafe_b64encode(msg.as_string().encode("utf-8")).decode(
        "utf-8"
    )

    try:
        service.users().messages().send(
            userId=os.environ.get("EMAIL"), body={"raw": raw_message}
        ).execute()
        print("Email bien envoyé")
    except HttpError as error:
        print(f"Failed to send the email: {error}")


if __name__ == "__main__":
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        pairs = []
        infos = open("user_infos.json", encoding="utf-8")
        user_infos = json.load(infos)
        while not is_valid_pairs(pairs):
            pairs = get_pairs()
        for pair in pairs:
            send_mail(pair[0], pair[1], user_infos, service)
    except HttpError as error:
        print(f"An error occurred: {error}")
