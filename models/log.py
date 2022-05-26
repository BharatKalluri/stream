import logging
from datetime import datetime

import parsedatetime
from mongoengine import Document, StringField, DateTimeField

logger = logging.getLogger(__name__)

cal = parsedatetime.Calendar()


class Log(Document):
    value = StringField(required=True)
    key = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    @staticmethod
    def create(value: str, key: str):
        return Log(value=str(value), key=key).save()
