import logging

from telegram import Message

from constants import firestore_db

logger = logging.getLogger(__name__)

stream_collection = firestore_db.collection('stream')


class Thought:
    def __init__(self, message: Message):
        message_id = message.message_id
        chat_id = message.chat_id
        thought_id = f"TELEGRAM_{chat_id}_{message_id}"

        self.content = message.text
        self.id = thought_id
        self.telegram_user_id = message.chat_id

    def to_json(self):
        return {
            'content': self.content,
            'telegram_user_id': self.telegram_user_id
        }

    def save(self):
        stream_collection \
            .document(self.id) \
            .set(self.to_json())

    def update_message(self, updated_content: str):
        stream_collection \
            .document(self.id) \
            .set({"content": updated_content})
