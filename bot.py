import logging

from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters

from constants import TELEGRAM_BOT_TOKEN
from handlers.store_thought_handler import store_thought_handler

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run the bot."""
    updater = Updater(TELEGRAM_BOT_TOKEN)

    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.text & (~Filters.command),
            store_thought_handler
        )
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
