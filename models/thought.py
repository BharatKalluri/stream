import base64
import logging
import parsedatetime
import uuid
from typing import Optional
from datetime import datetime

from constants import firestore_db

logger = logging.getLogger(__name__)

stream_collection = firestore_db.collection("stream")
cal = parsedatetime.Calendar()


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
        created_at, content = Thought.get_created_at_and_content_from_thought(
            self.content, self.created_at
        )
        thought = {
            "content": content,
            "telegram_user_id": self.telegram_user_id,
            "created_at": created_at,
        }
        if self.telegram_message_id:
            thought["telegram_message_id"] = self.telegram_message_id
        return thought

    @staticmethod
    def get_created_at_and_content_from_thought(
        content: str, created_at_timestamp: int
    ) -> [int, str]:
        if " @ " in content:
            time_struct, parse_status = cal.parse(content)
            if parse_status != 0:
                created_at_dt: datetime = datetime(*time_struct[:6])
                return int(created_at_dt.timestamp() * 1000), content.split(" @ ")[0]
        return created_at_timestamp, content

    def save(self):
        logger.debug(f"saving thought {self.to_json()}")
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
        document_raw = message_list[0]
        document_id = document_raw.id
        thought = Thought(**document_raw.to_dict())
        thought.content = updated_content
        logger.debug(f"updating thought {thought.to_json()}")
        stream_collection.document(document_id).update(thought.to_json())

    @staticmethod
    def print_all_messages_of_user(user_id: int, delimiter: str = "|"):
        message_list = list(
            stream_collection.where("telegram_user_id", "==", user_id).stream()
        )
        for m in [
            f"{(base64.b64encode(message.get('content').encode())).decode()}{delimiter}{message.get('created_at')}"
            for message in message_list
        ]:
            print(m)
