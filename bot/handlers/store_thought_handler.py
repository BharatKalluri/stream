from telegram import Update
from telegram.ext import CallbackContext

from models.thought import Thought
from utils import current_milli_time


def store_thought_handler(update: Update, context: CallbackContext):
    message = update.message
    thought = Thought(
        content=message.text,
        created_at=current_milli_time(),
        telegram_user_id=message.chat_id,
        telegram_message_id=message.message_id
    )

    try:
        thought.save()
    except BaseException as e:
        # Too broad exception
        update.message.reply_text(str(e))
