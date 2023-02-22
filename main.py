
import telebot

API_TOKEN = '6250424574:AAED9Do_CO8H6b4XXCrG7gOAmmSE5n-JMCg'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
    Привет""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()