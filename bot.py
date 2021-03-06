import logging

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from constants import TELEGRAM_BOT_TOKEN
from handlers.callback_query_handler import callback_query_handler
from handlers.store_thought_handler import store_thought_handler
from modules.reminders.reminder import setup_reminders
from modules.routines.routine_config import ROUTINE_CONFIG
from modules.routines.routine_constructor import routine_constructor
from utils import run_continuously

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    filename="thought-stream.log",
    filemode="a",
)
logger = logging.getLogger(__name__)


def main() -> None:
    updater: Updater = Updater(TELEGRAM_BOT_TOKEN)
    bot: Bot = updater.bot

    cease_continuous_run = run_continuously()

    setup_reminders(bot=bot)

    for routine_key in list(ROUTINE_CONFIG.keys()):
        updater.dispatcher.add_handler(routine_constructor(routine_key))

    updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))

    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.text & (~Filters.command) & (~Filters.update.edited_message),
            store_thought_handler,
        )
    )

    updater.start_polling()

    updater.idle()

    logger.info("Stopping reminder system")
    cease_continuous_run.set()


if __name__ == "__main__":
    main()
