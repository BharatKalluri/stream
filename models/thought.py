import logging

from telegram import Message

from constants import supabase_client

logger = logging.getLogger(__name__)

stream_table = supabase_client.table("stream")


class Thought:
    def __init__(self, message: Message):
        message_id = message.message_id
        chat_id = message.chat_id
        id = f"TELEGRAM_{chat_id}_{message_id}"

        self.content = message.text
        self.id = id
        self.telegram_user_id = message.chat_id

    @staticmethod
    def check_response_or_throw(response, error_message: str):
        if int(response["status_code"] / 200) == 2:
            logger.error(response)
            raise Exception(error_message)

    def to_json(self):
        return self.__dict__

    def save(self):
        data = stream_table.insert(self.to_json()).execute()
        self.check_response_or_throw(data, "could not save thought!")

    def update_message(self, updated_content: str):
        # Temporary solution until https://github.com/supabase/supabase-py/issues/30 if fixed
        data = stream_table.insert(
            {"id": self.id, "content": updated_content}, upsert=True
        ).execute()
        self.check_response_or_throw(data, "could not edit thought!")
