FIVE_SCALE_KEYBOARD = [[1, 2], [3, 4, 5]]
YES_NO_KEYBOARD = [["yes", "no"]]

ROUTINE_CONFIG = {
    "sleep": {
        1: {
            "question": "perceived happiness?",
            "hashtag": "#perceived_happiness",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        },
        2: {
            "question": "perceived stress?",
            "hashtag": "#perceived_happiness",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        },
        3: {
            "question": "worry about the future?",
            "hashtag": "#worry_about_future",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        },
        4: {
            "question": "How much did you go out of comfort zone today?",
            "hashtag": "#out_of_comfort_zone",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        },
    },
    "awake": {
        1: {
            "question": "sleep quality?",
            "hashtag": "#sleep_quality",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        },
        2: {
            "question": "any nightmares?",
            "hashtag": "#nightmares",
            "reply_keyboard": YES_NO_KEYBOARD,
        },
    },
    "mood": {
        1: {
            "question": "How are you feeling?",
            "hashtag": "#mood",
            "reply_keyboard": FIVE_SCALE_KEYBOARD,
        }
    },
}
