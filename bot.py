import logging

from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from constants import TELEGRAM_BOT_TOKEN
from handlers.login_command_handler import login_command_handler
from handlers.store_thought_handler import store_thought_handler
from handlers.update_thought_hander import update_thought_handler

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

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


if __name__ == "__main__":
    main()
