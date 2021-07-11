FIVE_SCALE_KEYBOARD = [[1, 2], [3, 4, 5]]
YES_NO_KEYBOARD = [["yes", "no"]]
COMMANDS_TO_RECORD_WHEN_INIT = ["sleep", "awake"]

ROUTINE_CONFIG = {
    "sleep": {
        "steps": [
            {
                "question": "How happy did you feel today, on a scale of 1 to 5?",
                "hashtag": "#perceived_happiness",
                "reply_keyboard": FIVE_SCALE_KEYBOARD,
            },
            {
                "question": "How stressed did you feel today?",
                "hashtag": "#perceived_stress",
                "reply_keyboard": {
                    5: "Very calm and aware",
                    4: "Calm & relaxed",
                    3: "Neutral",
                    2: "Lots to do",
                    1: "Stressed & Overwhelmed",
                    0: "Very stressed, not sure where to start",
                },
            },
            {
                "question": "When was your last caffeine drink?",
                "hashtag": "#last_caffeine_drink",
                "reply_keyboard": {
                    5: "Before 3pm",
                    4: "Before 5pm",
                    3: "Before 7pm",
                    2: "Before 9pm",
                    1: "Before 11pm",
                    0: "Later",
                },
            },
            {
                "question": "Did you nap today?",
                "hashtag": "#nap",
                "reply_keyboard": YES_NO_KEYBOARD,
            },
            {
                "question": "How healthy do you feel?",
                "hashtag": "#healthy_feel",
                "reply_keyboard": {
                    5: "Fully healthy & energized",
                    4: "Healthy",
                    3: "Might have a slight cold",
                    2: "Having a cold",
                    1: "Stayed home due to health",
                    0: "Actually sick",
                },
            },
            {
                "question": "Do you feel like you'd have needed more time by yourself?",
                "hashtag": "#time_by_myself",
                "reply_keyboard": {
                    5: "No",
                    4: "I've had just enough time",
                    3: "Good amount of time, could be more",
                    2: "Busy day, I need more time",
                    1: "Barely time for myself",
                    0: "No time by myself",
                },
            },
            {
                "question": "Did you feel like you were in control over your time and schedule?",
                "hashtag": "#control_of_time",
                "reply_keyboard": {
                    5: "In full control",
                    4: "In control, some constraints",
                    3: "A few constraints, but still in control",
                    2: "Average",
                    1: "Many constraints",
                    0: "Day was out of my control",
                },
            },
            {
                "question": "Do you feel like you need to socialize more?",
                "hashtag": "#need_to_socalize",
                "reply_keyboard": {
                    5: "No",
                    4: "Almost perfect amount",
                    3: "Socializing was okay",
                    2: "Feel like I should socialize more",
                    1: "Not enough socializing",
                    0: "Feeling isolated",
                },
            },
            {
                "question": "Did you learn/try something new? (skill or activity)",
                "hashtag": "#learning",
                "reply_keyboard": {
                    5: "Learned multiple new things",
                    4: "Learned some new things",
                    3: "Learned something new",
                    2: "Improved something existing",
                    1: "Didn't learn anything",
                    0: "I feel like I should learn more",
                },
            },
            {
                "question": "How much did you go out of comfort zone today?",
                "hashtag": "#out_of_comfort_zone",
                "reply_keyboard": {
                    5: "Did something(s) I was really scared about",
                    4: "Did something(s) I was worried about",
                    3: "Did something I wouldn't have done before",
                    2: "Did something new",
                    1: "Did smaller tweaks",
                    0: "Didn't do anything new",
                },
            },
            {
                "question": "Did you work on any technical challenges and problem solving?",
                "hashtag": "#problem_solving",
                "reply_keyboard": {
                    5: "Exciting challenges",
                    4: "Interesting challenges",
                    3: "Did some coding",
                    2: "No actual challenges",
                    1: "Just a little bit",
                    0: "Nothing",
                },
            },
            {
                "question": "How many (number) work meetings did you have today? This includes work-related phone calls",
                "hashtag": "#number_of_work_meetings",
            },
            {
                "question": "What do you think was the main influence to your mood ratings today? (can skip by entering 'skip')",
                "hashtag": "#mood_notes",
            },
            {
                "question": "What was your main accomplishment of today",
                "hashtag": "#main_accomplishment_today",
            },
            {
                "question": "Do you feel excited about what's ahead in the future?",
                "hashtag": "#exited_about_future",
                "reply_keyboard": YES_NO_KEYBOARD,
            },
            {
                "question": "worry about the future?",
                "hashtag": "#worry_about_future",
                "reply_keyboard": FIVE_SCALE_KEYBOARD,
            },
        ]
    },
    "awake": {
        "steps": [
            {
                "question": "sleep quality?",
                "hashtag": "#sleep_quality",
                "reply_keyboard": {
                    5: "Excellent, feeling refreshed",
                    4: "Great, feeling good",
                    3: "Good, slightly above average",
                    2: "Solid, slightly tired",
                    1: "Tired, restless sleep",
                    0: "Miserable",
                },
            },
            {
                "question": "any nightmares?",
                "hashtag": "#nightmares",
                "reply_keyboard": YES_NO_KEYBOARD,
            },
        ]
    },
    "mood": {
        "record_init": False,
        "steps": [
            {
                "question": "How are you feeling?",
                "hashtag": "#mood",
                "reply_keyboard": {
                    5: "pumped, energized",
                    4: "happy, excited",
                    3: "good",
                    2: "okay",
                    1: "sad, unhappy",
                    0: "nervous",
                },
            }
        ],
    },
}
