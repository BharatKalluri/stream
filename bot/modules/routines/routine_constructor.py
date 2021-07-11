import logging
from typing import Optional

from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
    MessageHandler,
    Filters,
    CommandHandler,
)

from models.thought import Thought
from modules.routines.routine_config import ROUTINE_CONFIG
from utils import current_milli_time

logger = logging.getLogger(__name__)


def routine_constructor(routine_name: str) -> ConversationHandler:
    routine_config: Optional[dict[int, dict[str, str]]] = ROUTINE_CONFIG.get(
        routine_name
    )
    steps: list[int] = list(routine_config.keys())

    def cancel_conversation(update: Update, context: CallbackContext) -> int:
        update.message.reply_text("Bye!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    def start_conversation(update: Update, context: CallbackContext) -> int:
        question_config = routine_config.get(1, {})
        question_in_queue = question_config.get("question")
        reply_keyboard_config = question_config.get("reply_keyboard")

        reply_keyboard_markup = (
            ReplyKeyboardMarkup(reply_keyboard_config, one_time_keyboard=True)
            if reply_keyboard_config
            else ReplyKeyboardRemove()
        )
        update.message.reply_text(
            f"Lets get started! {question_in_queue} (/cancel)",
            reply_markup=reply_keyboard_markup,
        )
        return 1

    def step_qa_constructor(
        display_text_for_step: str, next_step_pointer_for_step: Optional[int]
    ):
        def func(update: Update, context: CallbackContext) -> int:
            user = update.message.from_user

            final_question_step_number = list(routine_config.keys())[-1]

            last_question_config = (
                routine_config.get(next_step_pointer_for_step - 1)
                if next_step_pointer_for_step != -1
                else routine_config.get(final_question_step_number)
            )

            if last_question_config:
                last_question_hashtag = last_question_config.get("hashtag")
                message_to_store = f"{last_question_hashtag} {update.message.text}"
                Thought(
                    content=message_to_store,
                    telegram_user_id=user.id,
                    created_at=current_milli_time(),
                    telegram_message_id=None,
                ).save()
                update.message.reply_text(f"stored: {message_to_store}")

            question_config = routine_config.get(next_step_pointer_for_step, {})
            reply_keyboard_config = question_config.get("reply_keyboard")

            next_question = (
                f'{question_config.get("question")} (/cancel)'
                if question_config.get("question")
                else "Thanks!"
            )
            reply_keyboard_markup = (
                ReplyKeyboardMarkup(reply_keyboard_config, one_time_keyboard=True)
                if reply_keyboard_config
                else ReplyKeyboardRemove()
            )

            update.message.reply_text(next_question, reply_markup=reply_keyboard_markup)
            return next_step_pointer_for_step

        return func

    conversation_states = {}
    final_step = steps[-1]
    for step in steps:
        step_config = routine_config.get(step)
        display_text = step_config.get("question")
        next_step_pointer = step + 1 if step != final_step else ConversationHandler.END
        conversation_states[step] = [
            MessageHandler(
                Filters.text & ~Filters.command,
                step_qa_constructor(
                    display_text_for_step=display_text,
                    next_step_pointer_for_step=next_step_pointer,
                ),
            )
        ]

    return ConversationHandler(
        entry_points=[CommandHandler(routine_name, start_conversation)],
        states=conversation_states,
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
