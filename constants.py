import json
import os
from enum import Enum

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
FIREBASE_CERT = json.loads(os.getenv("FIREBASE_CERT"))

cred = credentials.Certificate(FIREBASE_CERT)

firebase_admin.initialize_app(cred)
firestore_db = firestore.client()


class ReminderEventType(Enum):
    MOOD = "MOOD"
    SLEEP = "SLEEP"
    AWAKE = "AWAKE"


REMINDER_EVENT_TO_MESSAGE_MAP = {
    ReminderEventType.MOOD: "Record your mood using /mood",
    ReminderEventType.SLEEP: "Close your day by filling in /sleep",
    ReminderEventType.AWAKE: "Good morning! Hit /awake and fill in some deets!",
}
