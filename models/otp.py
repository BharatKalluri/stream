import logging
from random import SystemRandom

from supabase_py.lib.query_builder import SupabaseQueryBuilder

from constants import supabase_client

otp_table: SupabaseQueryBuilder = supabase_client.table("otp")

logger = logging.getLogger(__name__)


class Otp:
    def __init__(self, for_telegram_user_id: int) -> None:
        self.otp = self.generate_otp()
        self.telegram_user_id = for_telegram_user_id

    @staticmethod
    def check_response_or_throw(response, error_message: str) -> None:
        if int(response["status_code"] / 200) == 2:
            logger.error(response)
            raise Exception(error_message)

    @staticmethod
    def generate_otp() -> int:
        return SystemRandom().randint(100000, 999999)

    def to_json(self) -> dict:
        return self.__dict__

    def save(self) -> None:
        response = otp_table.insert(self.to_json()).execute()
        self.check_response_or_throw(response, "generated otp is invalid :(")
