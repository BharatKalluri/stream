import json

from telegram import Update
from telegram.ext import CallbackContext

from handlers.log_mood_handler import MoodEvent
from models.thought import Thought
from utils import current_milli_time


def callback_query_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query_data = json.loads(query.data)
    event = query_data.get("event")
    event_value = query_data.get("value")

    if event == MoodEvent.event_name:
        thought = Thought(
            content=f"#mood {event_value}",
            telegram_user_id=update.effective_user.id,
            created_at=current_milli_time(),
            telegram_message_id=None,
        )
        thought.save()
        query.edit_message_text(text=f"Logged mood @ {event_value}")
    else:
        query.edit_message_text(text="did not understand a word!")
