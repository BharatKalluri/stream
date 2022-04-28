from telegram import Update
from telegram.ext import CallbackContext

from models.log import Log


def store_thought_handler(update: Update, context: CallbackContext):
    message = update.message
    try:
        # TODO: make the key a const
        Log.create(
            value=message.text,
            key="raw_thought",
        )
    except BaseException as e:
        # Too broad exception
        update.message.reply_text(str(e))
