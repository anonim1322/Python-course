import random
import telebot
from telebot import types

bot = telebot.TeleBot("ТОКЕН БОТУ")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Відправити стікер")
    bot.send_message(message.chat.id, "Стікер", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "відправити стікер":
        bot.send_sticker(
            message.chat.id,
            random.choice([
                           "CAACAgIAAxkBAAEFSFdi0UFa9zhxfMIdAcUvTLYIjWafkgACsgEAAhZCawqceQABhqhR6VIpBA",
                           "CAACAgIAAxkBAAEFSFli0UKmsMvsq20o55pvyumsk19EFwACTgIAAladvQow_mttgTIDbykE",
                           "CAACAgIAAxkBAAEFSF1i0UK5Ek-D_Rpwd3EbGPsNjuiu4QACRgADWbv8JRLr_Wbcq939KQQ",
                           "CAACAgIAAxkBAAEFSF9i0URyWa6lJ5st5gxANDeclKQHYQACVgMAArrAlQVLc5BvAzFr7ykE",
                           "CAACAgEAAxkBAAEFSGNi0USqnXaMJA1PWHoDR7iFka-DgQAC9AEAAjgOghGFRlSELmKpcCkE",
                           "CAACAgIAAxkBAAEFSGVi0UUQF3IL6iaIQAgX0zH8mo6vGwACCQEAAladvQrWZlyD1z-oHSkE",
                           "CAACAgIAAxkBAAEFSGdi0UVVd80thsvIjeQrNMqirdiIKwAC5AcAAkb7rATqvj3pHSd59SkE",
                           "CAACAgEAAxkBAAEFSGli0UVzke_RU1uvj2AmEDspHJwe0QACJgEAAjgOghFsuLJgLC4WcykE",
                           "CAACAgIAAxkBAAEFSGti0UWbpTTjjB0rRbXmoUL-mHstjgACCQADwDZPE-_NG6JK_3GVKQQ",
                           "CAACAgIAAxkBAAEFSG1i0UYX1tdN8cvivtLLIpdC-NSsNQACgQADRA3PF8jAOMgk_BkZKQQ",
                           "CAACAgIAAxkBAAEFSG9i0UZAZrGoU5QZl5aSCR4He16MGgACGQADrWW8FGVA9WQz8jIpKQQ",
                           "CAACAgIAAxkBAAEFSHFi0UZWMt2Tul3MyqNJTSat0CXRuQACTAADwDZPE6kHYdoJW8ToKQQ",
                           "CAACAgIAAxkBAAEFSHNi0UZpQD0pYYKL6p8_ZJIQTDaVOQACcQADDbbSGXow3EPisBCnKQQ",
                           ])
            )

bot.polling(none_stop=True)