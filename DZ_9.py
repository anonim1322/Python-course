import time
import telebot
from telebot import types

bot = telebot.TeleBot("ТОКЕН БОТУ")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Це таймер")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Таймер")
    bot.send_message(message.chat.id, "Таймер", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "таймер":
        bot.send_message(message.chat.id, "Час пійшов")
        for i in range(5):
            time.sleep(60)
            bot.send_message(message.chat.id, f"Залишилося {5 - i} хвилин")

        time.sleep(60)
        bot.send_message(message.chat.id, "Час вийшов")


bot.polling(none_stop=True)