import telebot

bot = telebot.TeleBot("ТОКЕН БОТУ")
@bot.message_handler(commands="start")
def start(message):
    bot.send_message(message.chat.id, "Бот успішно працюе")

@bot.message_handler(commands="name")
def name(message):
    bot.send_message(message.chat.id, "Розробник: Андрій Ковальський, нік в Zoom: Andrey, нік в Viber: Andrey Kovalskiy, нік в Telegram: Andrey")

@bot.message_handler(content_types="text")
def name(message):
    if message.text.lower() == "андрій":
        bot.send_message(message.chat.id, "Це мій розробник :)")

bot.polling(none_stop=True)
