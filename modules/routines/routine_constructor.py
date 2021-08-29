import logging
from typing import Optional

from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, Message
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


def _get_reply_keyboard_config_from_question(question_config: dict):
    reply_keyboard_config = question_config.get("reply_keyboard")

    if isinstance(reply_keyboard_config, dict):
        reply_keyboard_config: list[list[str]] = [
            [el] for el in reply_keyboard_config.values()
        ]

    reply_keyboard_markup = (
        ReplyKeyboardMarkup(reply_keyboard_config, one_time_keyboard=True)
        if reply_keyboard_config
        else ReplyKeyboardRemove()
    )
    return reply_keyboard_markup


def _get_rating_from_response(question_config: dict, message: Message):
    question_reply_keyboard_config = question_config.get("reply_keyboard")
    text_response = message.text
    if isinstance(question_reply_keyboard_config, dict):
        inverted_dict = {v: k for k, v in question_reply_keyboard_config.items()}
        text_response = inverted_dict.get(text_response)
    return text_response


def routine_constructor(routine_name: str) -> ConversationHandler:
    routine_config_step_list: list[dict] = ROUTINE_CONFIG.get(routine_name).get("steps")
    routine_steps_config = {(k + 1): v for k, v in enumerate(routine_config_step_list)}
    steps: list[int] = list(routine_steps_config.keys())
    should_record_init = ROUTINE_CONFIG.get(routine_name).get("record_init", True)

    def cancel_conversation(update: Update, context: CallbackContext) -> int:
        update.message.reply_text("Bye!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    def start_conversation(update: Update, context: CallbackContext) -> int:
        question_config = routine_steps_config.get(1, {})
        question_in_queue = question_config.get("question")

        if should_record_init is True:
            message_to_store = update.message.text.replace('/', '#')
            Thought(
                content=message_to_store,
                telegram_user_id=update.effective_user.id,
                created_at=current_milli_time(),
                telegram_message_id=None,
            ).save()

        update.message.reply_text(
            f"Lets get started! {question_in_queue} (/cancel)",
            reply_markup=_get_reply_keyboard_config_from_question(question_config),
        )

        return 1

    def step_qa_constructor(next_step_pointer_for_step: Optional[int]):
        def func(update: Update, context: CallbackContext) -> int:
            user = update.message.from_user

            final_question_step_number = list(routine_steps_config.keys())[-1]

            last_question_config = (
                routine_steps_config.get(next_step_pointer_for_step - 1)
                if next_step_pointer_for_step != -1
                else routine_steps_config.get(final_question_step_number)
            )

            if last_question_config:
                last_question_hashtag = last_question_config.get("hashtag")
                text_response = _get_rating_from_response(
                    last_question_config, update.message
                )

                message_to_store = f"{last_question_hashtag} {text_response}"
                should_save = str(text_response).lower() != "skip"
                if should_save is True:
                    Thought(
                        content=message_to_store,
                        telegram_user_id=user.id,
                        created_at=current_milli_time(),
                        telegram_message_id=None,
                    ).save()
                else:
                    update.message.reply_text("Skipped")

            question_config = routine_steps_config.get(next_step_pointer_for_step, {})

            next_question = (
                f'{question_config.get("question")} (/cancel)'
                if question_config.get("question")
                else "Thanks!"
            )

            update.message.reply_text(
                next_question,
                reply_markup=_get_reply_keyboard_config_from_question(question_config),
            )
            return next_step_pointer_for_step

        return func

    conversation_states = {}
    final_step = steps[-1]
    for step in steps:
        step_config = routine_steps_config.get(step)
        display_text = step_config.get("question")
        next_step_pointer = step + 1 if step != final_step else ConversationHandler.END
        conversation_states[step] = [
            MessageHandler(
                Filters.text & ~Filters.command,
                step_qa_constructor(
                    next_step_pointer_for_step=next_step_pointer,
                ),
            )
        ]

    return ConversationHandler(
        entry_points=[CommandHandler(routine_name, start_conversation)],
        states=conversation_states,
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
