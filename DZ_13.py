import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт!")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Запис", "Список")
    bot.send_message(message.chat.id, "Запис список", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def text(message):
    plan_list = []

    if message.text.lower() == "запис":
        bot.send_message(message.chat.id, "Запишіть план:")
        plan_list.append(message.text)

    elif message.text.lower() == "список":
        if plan_list:
            bot.send_message(message.chat.id, "Ваши плани:")

            for i in plan_list:
                bot.send_message(message.chat.id, i)

        elif plan_list == []:
            bot.send_message(message.chat.id, "У вас нема планів")

bot.polling(none_stop=True)