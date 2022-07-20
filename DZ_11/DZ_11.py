import telebot
from telebot import types
import random

bot = telebot.TeleBot("ТОКЕН БОТУ")

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Привіт!")
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row("Фото", "Мемний відос")
	bot.send_message(message.chat.id, "Фото мем", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def text(message):
	if message.text.lower() == "фото":
		bot.send_photo(message.chat.id, open(random.choice(["photo1.png", "photo2.png", "photo3.png", "photo4.png"]), "rb"))

	elif message.text.lower() == "мемний відос":
		bot.send_video(message.chat.id, open("video.mp4", "rb"))

bot.polling(none_stop=True)