from telegram import Update, User
from telegram.ext import CallbackContext

from models.thought import Thought


def store_thought_handler(update: Update, context: CallbackContext):
    thought = update.message.text
    telegram_user: Optional[User] = update.effective_user
    telegram_user_id: int = telegram_user.id
    thought = Thought(content=thought, telegram_user_id=telegram_user_id)
    try:
        thought.save()
    except BaseException as e:
        # Too broad exception
        update.message.reply_text('Something went wrong')
