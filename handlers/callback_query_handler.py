from telegram import Update
from telegram.ext import CallbackContext


def callback_query_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="did not understand a word!")
