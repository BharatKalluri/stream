import logging
from random import SystemRandom

from constants import firestore_db

otp_collection = firestore_db.collection('otp')

logger = logging.getLogger(__name__)


class Otp:
    def __init__(self, for_telegram_user_id: int) -> None:
        self.otp = self.generate_otp()
        self.telegram_user_id = for_telegram_user_id

    @staticmethod
    def generate_otp() -> int:
        return SystemRandom().randint(100000, 999999)

    def to_json(self) -> dict:
        return self.__dict__

    def save(self) -> None:
        otp_collection \
            .document(f'{self.telegram_user_id}_{self.otp}') \
            .set(self.to_json())
