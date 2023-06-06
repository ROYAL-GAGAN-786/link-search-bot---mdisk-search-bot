import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 25830285))
    API_HASH = os.environ.get("API_HASH", "0cbcabbf1b9c56a4dfc4b8950d584a2a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5827438477:AAH__CXXOeqv4Xkknvg6kiL6yYa0WrrbCks")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOHQBu3vYsA7TkvELHqyaq1RL5WAXZtpNikD0Mg0zh1iTwnCmR-a_iY3_XeGsf6AgpiCwPsPZCVPqHHO0YUbA4-ybq9j70ku_Cevm8XWcRPMlCRzMbVsDSLhgq1s8vUyOtntC_RFqwW1VDJwMBO2Uf0boIP8PfH9Bz9geZjGh7fXySLavXy2mmBzSuRDbLeYJT99zGY9UvizCr-rUBaLqS4Urk7qscjXcPGqb6qtONvKB-jmAncXm3PNAzcJcB_FO7QDQ1lFr19rKekBOUZN68p-kujHmzWOzbMjYGL1djpQjym_VeU8ewZM_YBkApM0TxqsItee-Nsz7CA1ZnKSFI4BBFT0=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TERE_BOX_MOVIES_SEARCH_BOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5124332598"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Mdiskdb-mongo:777@cluster0.sn5inqp.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='@ROYAL_PREET_MEHRA_7868'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='t.me/ROYAL_PREET_MEHRA_7868'>MOVIES VILLA</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='t.me/ROYAL_PREET_MEHRA_7868'>MOVIES VILLA</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @ROYAL_PREET_MEHRA_7868</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @ROYAL_PREET_MEHRA_7868</a></b>
"""

