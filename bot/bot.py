import logging

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CommandHandler,
    CallbackQueryHandler,
)

from constants import TELEGRAM_BOT_TOKEN
from handlers.callback_query_handler import callback_query_handler
from handlers.log_mood_handler import log_mood_handler
from handlers.login_command_handler import login_command_handler
from handlers.start_command_handler import start_command_handler
from handlers.store_thought_handler import store_thought_handler
from handlers.update_thought_hander import update_thought_handler
from modules.reminders.reminder import setup_reminders
from modules.routines.routine_config import ROUTINE_CONFIG
from modules.routines.routine_constructor import routine_constructor
from utils import run_continuously

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    updater: Updater = Updater(TELEGRAM_BOT_TOKEN)
    bot: Bot = updater.bot

    cease_continuous_run = run_continuously()

    setup_reminders(bot=bot)

    for routine_key in list(ROUTINE_CONFIG.keys()):
        updater.dispatcher.add_handler(routine_constructor(routine_key))

    updater.dispatcher.add_handler(CommandHandler("start", start_command_handler))
    updater.dispatcher.add_handler(CommandHandler("log_mood", log_mood_handler))

    updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))

    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.text & (~Filters.command) & (~Filters.update.edited_message),
            store_thought_handler,
        )
    )
    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.update & (~Filters.command) & Filters.text, update_thought_handler
        )
    )
    updater.dispatcher.add_handler(CommandHandler("login", login_command_handler))

    updater.start_polling()

    updater.idle()

    logger.info("Stopping reminder system")
    cease_continuous_run.set()


if __name__ == "__main__":
    main()
