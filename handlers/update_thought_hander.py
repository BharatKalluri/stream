from telegram import Update
from telegram.ext import CallbackContext

from models.thought import Thought


def update_thought_handler(update: Update, context: CallbackContext):
    message = update.edited_message
    try:
        Thought.update_message(
            telegram_message_id=message.message_id,
            telegram_user_id=message.chat_id,
            updated_content=message.text,
        )
    except BaseException as e:
        # Too broad exception
        update.message.reply_text(str(e))
