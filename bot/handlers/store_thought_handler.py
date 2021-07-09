from telegram import Update
from telegram.ext import CallbackContext

from models.thought import Thought


def store_thought_handler(update: Update, context: CallbackContext):
    thought = Thought(message=update.message)

    try:
        thought.save()
    except BaseException as e:
        # Too broad exception
        update.message.reply_text(str(e))
