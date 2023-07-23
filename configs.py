import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 25830285))
    API_HASH = os.environ.get("API_HASH", "0cbcabbf1b9c56a4dfc4b8950d584a2a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6223100452:AAETcNqFYN11AXMI1Is8YdiNe_yJusACn6s")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQDa9Z8ARkHn4q44be6IimS4enTi5ubKZyzMctPyLLvcXpXQtA2hrpWqbfEjHPqBVOfipfJCXpQpDQrmqG1lNiHUEYw5dq991X2APs3t1xtZrAWOyFgy6mZ1SWqHtj8C-GtEuW-A__Li5PoOke5sum2slttXcj2E9zMUcNlZxOXKpTcr4zNWm0WQgS41uTUtvky1mUefUofBQxXkwEPbK5XoHUDxhtyE4Vxc9uAD-_9dmU9C0HFkaLRZJ2OFe0J-1HHMkvWXF2nD55hEY4SW1NWrBmqqqKzygWg5zom7mAf3PSSwz7vLUIN2aXoj_Vdmxwq2ddeRIiN6XLUApUYeg-1egf0PSgAAAAFXqjyAAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001885390961))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TERE_BOX_MOVIES_SEARCH_BOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5124332598"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://786:786@cluster0.i6dbky4.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001279636969)
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

