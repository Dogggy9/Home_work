import telebot
from telebot import types

TOKEN = "5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Я здороваюсь и рассказываю о возможностях")

@bot.message_handler(commands=['about_author'])
def about_author(message):
    bot.reply_to(message, "Кратко рассказываю о себе")

@bot.message_handler(commands=['get_keyboard'])
def get_keyboard(message):
    keyBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Кнопка 1")
    key2 = types.KeyboardButton("Кнопка 2")
    key3 = types.KeyboardButton("Кнопка 3")
    key4 = types.KeyboardButton("Кнопка 4")
    keyBoard.add(key1, key2, key3, key4)
    bot.send_message(message.chat.id, "возврат клавиатуры из 2-3 кнопок", reply_markup=keyBoard)

@bot.message_handler(commands=['get_keyboard_inline'])
def get_keyboard_inline(message):
    keyBoard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="Кнопка 1")
    key2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="Кнопка 2")
    key3 = types.InlineKeyboardButton(text="Кнопка 3", callback_data="Кнопка 3")
    key4 = types.InlineKeyboardButton(text="Кнопка 4", callback_data="Кнопка 4")
    keyBoard.add(key1, key2, key3, key4)
    bot.send_message(message.chat.id, "возврат клавиатуры из 2-3 кнопок как сообщение", reply_markup=keyBoard)

@bot.callback_query_handler(func=lambda m:True)
def inline(message):
    if message.data == "Кнопка 1":
        bot.send_message(message.chat.id, 'Ты нажал кнопка 1')
    elif message.data == "Кнопка 2":
        pass
    elif message.data == "Кнопка 3":
        pass
    elif message.data == "Кнопка 4":
        pass

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()


