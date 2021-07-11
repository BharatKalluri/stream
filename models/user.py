import uuid
from typing import List

from google.cloud.firestore_v1 import DocumentSnapshot, CollectionReference

from constants import firestore_db

user_collection: CollectionReference = firestore_db.collection("user")


class User:
    def __init__(self, telegram_user_id: int):
        self.telegram_user_id = telegram_user_id

    def to_json(self):
        return {"telegram_user_id": self.telegram_user_id}

    def get(self) -> List[DocumentSnapshot]:
        return list(
            user_collection.where(
                "telegram_user_id", "==", self.telegram_user_id
            ).stream()
        )

    def create_if_not_exists(self):
        existing_user = self.get()
        if len(existing_user) > 0:
            return
        user_collection.document(str(uuid.uuid4())).set(self.to_json())

    @staticmethod
    def get_telegram_ids():
        user_list: List[DocumentSnapshot] = list(user_collection.stream())
        return [el.get("telegram_user_id") for el in user_list]
