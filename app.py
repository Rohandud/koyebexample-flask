import telebot
from flask import Flask, request
import random
from indic_transliteration import sanscript
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Retrieve Telegram bot token from environment variables
TOKEN = os.getenv('TOKEN')

# Initialize Telebot with the bot token
bot = telebot.TeleBot(TOKEN, threaded=False)

# Initialize the bot
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if flask.request.method == 'POST':
        update = telebot.types.Update.de_json(flask.request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        return 'Hello', 200

# Define a message handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    print(f"start {user_name}")
    bot.reply_to(message, f"Hey {user_name}!")

# Define a function to sanitize messages
def sanitize_message(message):
    if message.endswith(" ||"):
        return message[:-3]  # Remove the last 3 characters (" ||")
    else:
        return message

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
