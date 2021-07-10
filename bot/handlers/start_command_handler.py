from telegram import Update
from telegram.ext import CallbackContext

from models.user import User


def start_command_handler(update: Update, context: CallbackContext):
    telegram_user_id = update.message.chat_id
    user = User(telegram_user_id=telegram_user_id)
    user.create_if_not_exists()
