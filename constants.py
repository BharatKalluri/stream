import os
from enum import Enum

from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = 571637265
MONGODB_URL = os.getenv("MONGODB_URL")
connect(host=MONGODB_URL)


class ReminderEventType(Enum):
    MOOD = "MOOD"
    SLEEP = "SLEEP"
    AWAKE = "AWAKE"


REMINDER_EVENT_TO_MESSAGE_MAP = {
    ReminderEventType.MOOD: "Record your mood using /mood",
    ReminderEventType.SLEEP: "Close your day by filling in /sleep",
    ReminderEventType.AWAKE: "Good morning! Hit /awake and fill in some deets!",
}
