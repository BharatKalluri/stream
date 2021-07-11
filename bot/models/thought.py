import logging
import uuid
from typing import Optional

from constants import firestore_db

logger = logging.getLogger(__name__)

stream_collection = firestore_db.collection("stream")


class Thought:
    def __init__(
        self,
        content: str,
        telegram_user_id: int,
        created_at: int,
        telegram_message_id: Optional[int],
    ):
        self.content = content
        self.id = str(uuid.uuid4())
        self.telegram_user_id = telegram_user_id
        self.telegram_message_id = telegram_message_id
        self.created_at = created_at

    def to_json(self) -> dict:
        thought = {
            "content": self.content,
            "telegram_user_id": self.telegram_user_id,
            "created_at": self.created_at,
        }
        if self.telegram_message_id:
            thought["telegram_message_id"] = self.telegram_message_id
        return thought

    def save(self):
        stream_collection.document(self.id).set(self.to_json())

    @staticmethod
    def update_message(
        telegram_user_id: int, telegram_message_id: int, updated_content: str
    ):
        message_list = list(
            stream_collection.where("telegram_user_id", "==", telegram_user_id)
            .where("telegram_message_id", "==", telegram_message_id)
            .stream()
        )
        if len(message_list) == 0:
            return
        document_id = message_list[0].id
        stream_collection.document(document_id).update({"content": updated_content})
