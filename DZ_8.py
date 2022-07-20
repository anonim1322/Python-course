import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot("5547308975:AAH4ZWgU0dVdavzouXvint80FIRU7gvNQq8")

@bot.message_handler(commands=["start"])
def welcome(message):
  bot.send_message(message.chat.id, "Привіт! Це гра камінь ножиці папір")
  keyboard = types.ReplyKeyboardMarkup(
                                       resize_keyboard=True,
                                       input_field_placeholder="Камінь ножниці бумага"
                                       )
  keyboard.row("Камінь","Ножиці")
  keyboard.row("Бумага")
  bot.send_message(message.chat.id, "Камінь ножниці бумага", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def text(message):
  computer = choice(["Камінь", "Ножиці", "Бумага"])
  if message.text == "Камінь":
    if computer == "Бумага":
      bot.send_message(message.chat.id, f"Ви програли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Камінь":
      bot.send_message(message.chat.id, f"Нічья, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Ножиці":
      bot.send_message(message.chat.id, f"Ви виграли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

  elif message.text == "Ножиці":
    if computer == "Бумага":
      bot.send_message(message.chat.id, f"Ви виграли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Камінь":
      bot.send_message(message.chat.id, f"Ви програли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Ножиці":
      bot.send_message(message.chat.id, f"Нічья, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

  elif message.text == "Бумага":
    if computer == "Бумага":
      bot.send_message(message.chat.id, f"Нічья, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Камінь":
      bot.send_message(message.chat.id, f"Ви виграли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

    elif computer == "Ножиці":
      bot.send_message(message.chat.id, f"Ви програли, компютер вибрав {computer}")
      computer = choice(["Камінь", "Ножиці", "Бумага"])

bot.polling(none_stop = True)