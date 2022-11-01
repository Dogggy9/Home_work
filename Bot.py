import telebot
from telebot import types
from moduls.seting import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.reply_to(message, """Я здороваюсь и рассказываю о возможностях
    /about_author, /get_keyboard, /get_keyboard_inline""")


@bot.message_handler(commands=['about_author'])
def about_author(message: types.Message):
    bot.send_message(message.chat.id, "Кратко рассказываю о себе")


@bot.message_handler(commands=['get_keyboard'])
def get_keyboard(message: types.Message):
    keyBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("1 кнопка")
    key2 = types.KeyboardButton("2 кнопка")
    key3 = types.KeyboardButton("3 кнопка")
    key4 = types.KeyboardButton("/help")
    keyBoard.add(key1, key2, key3, key4)
    bot.send_message(message.chat.id, "возврат клавиатуры из 2-3 кнопок", reply_markup=keyBoard)


@bot.message_handler(commands=['get_keyboard_inline'])
def get_keyboard_inline(message: types.Message):
    inlinekeyBoard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="Кнопка 1")
    key2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="Кнопка 2")
    key3 = types.InlineKeyboardButton(text="Кнопка 3", callback_data="Кнопка 3")
    key4 = types.InlineKeyboardButton(text="Кнопка 4", callback_data="Кнопка 4")
    inlinekeyBoard.add(key1, key2, key3, key4)
    bot.send_message(message.chat.id, "возврат клавиатуры из 2-3 кнопок как сообщение", reply_markup=inlinekeyBoard)


@bot.callback_query_handler(func=lambda m: True)
def inline(call: types.CallbackQuery):
    if call.data == "Кнопка 1":
        bot.send_message(call.message.chat.id, 'Ты нажал кнопку 1')
    elif call.data == "Кнопка 2":
        bot.send_message(call.message.chat.id, 'Ты нажал кнопку 2')
    elif call.data == "Кнопка 3":
        bot.send_message(call.message.chat.id, 'Ты нажал кнопку 3')
    elif call.data == "Кнопка 4":
        bot.send_message(call.message.chat.id, 'Ты нажал кнопку 4')


@bot.message_handler(content_types=['text'])
def hi_user(message: types.Message):
    if message.text == "1 кнопка":
        bot.send_message(message.chat.id, 'Ты нажал 1 кнопку')
    elif message.text == "2 кнопка":
        bot.send_message(message.chat.id, 'Ты нажал 2 кнопку')
    elif message.text == "help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.chat.id, message.text)


# @bot.message_handler(func=lambda m: True)
# def echo_all(call):
#     bot.send_message(call.chat.id, call.text)

bot.infinity_polling()
