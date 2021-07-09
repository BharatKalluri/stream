import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

cred = credentials.Certificate("./firebase-admin-key.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()
