import telebot
import json
from flask import Flask
import random
from indic_transliteration import sanscript
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
app = Flask(__name__)
TOKEN = os.getenv('TOKEN')
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

@bot.message_handler(commands=['start'])
def start(message):
  user_name = message.from_user.first_name
  print("start "+user_name)
  bot.reply_to(message, "Hey "+user_name +"")
def sanitize_message(message):
    if message.endswith(" ||"):
        return message[:-3]  # Remove the last 3 characters (" ||")
    else:
        return message

if __name__ == "__main__":
    app.run()
