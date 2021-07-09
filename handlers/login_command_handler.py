from telegram import Update
from telegram.ext import CallbackContext

from models.otp import Otp


def login_command_handler(update: Update, context: CallbackContext):
    telegram_user_id = update.message.chat_id
    generated_otp = Otp(telegram_user_id)
    generated_otp.save()
    update.message.reply_text(
        f"User ID: {generated_otp.telegram_user_id}, OTP: {generated_otp.otp}"
    )