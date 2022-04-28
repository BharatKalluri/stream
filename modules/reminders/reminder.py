import logging

import schedule
from telegram import Bot

from constants import ReminderEventType, REMINDER_EVENT_TO_MESSAGE_MAP, TELEGRAM_USER_ID
from modules.reminders.reminder_config import REMINDER_CONFIG

logger = logging.getLogger(__name__)


def reminder(event_type: ReminderEventType, bot: Bot):
    message = REMINDER_EVENT_TO_MESSAGE_MAP.get(event_type)
    bot.send_message(text=message, chat_id=TELEGRAM_USER_ID)


def setup_reminders(bot: Bot):
    for reminder_config in REMINDER_CONFIG:
        every_config = reminder_config.get("every", 1)
        unit_config = reminder_config.get("unit")
        at_config = reminder_config.get("at")

        job = schedule.every(interval=every_config)
        job = getattr(job, unit_config) if unit_config else job
        job = job.at(at_config) if at_config else job

        job.do(reminder, event_type=reminder_config.get("event_type"), bot=bot)
