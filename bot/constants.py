import os
from enum import Enum

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

cred = credentials.Certificate("./firebase-admin-key.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()


class ReminderEventType(Enum):
    MOOD = "MOOD"


REMINDER_EVENT_TO_MESSAGE_MAP = {
    ReminderEventType.MOOD: "note your mood on a scale of 1 to 5 using /log_mood"
}
