from supabase_py.lib.query_builder import SupabaseQueryBuilder

from constants import supabase_client

stream_table: SupabaseQueryBuilder = supabase_client.table("stream")


class Thought:
    def __init__(self, content: str, telegram_user_id: int):
        self.content = content
        self.telegram_user_id = telegram_user_id

    def to_json(self):
        return self.__dict__

    def save(self):
        data = stream_table.insert(
            self.to_json()
        ).execute()
        if data['status_code'] != 201:
            raise Exception(f'Something went wrong!')
