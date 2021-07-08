from telegram import Update
from telegram.ext import CallbackContext

from models.thought import Thought


def update_thought_handler(update: Update, context: CallbackContext):
    thought = Thought(update.edited_message)
    try:
        thought.update_message(update.edited_message.text)
    except BaseException as e:
        # Too broad exception
        update.message.reply_text(str(e))
