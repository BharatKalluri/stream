import json

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


class MoodEvent:
    event_name = "mood"

    def __init__(self, value: int):
        self.event = MoodEvent.event_name
        self.value = value

    def to_dict(self):
        return self.__dict__


def log_mood_handler(update: Update, context: CallbackContext) -> None:
    keyboard_entries = [
        InlineKeyboardButton(str(el), callback_data=json.dumps(MoodEvent(el).to_dict()))
        for el in [1, 2, 3, 4, 5]
    ]
    keyboard = [keyboard_entries]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("How are you feeling?", reply_markup=reply_markup)
