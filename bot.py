import telebot
import config
import random
from model import generate_sentence

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Обратиться к Петру Михайловичу")

    markup.add(item1)

    bot.send_message(message.chat.id, "Поехали, {0.first_name}!\nЯ - <b>{1.first_name}</b>-бот".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def foo(message):
    if message.chat.type == 'private':
        if message.text == 'Обратиться к Петру Михайловичу':
            bot.send_message(message.chat.id, generate_sentence())

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'Вот и отличненько 👍')
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Бывает 😢')
#
#             # remove inline buttons
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😄 Как делишки?", reply_markup=None)
#             # show alert
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Test")
#     except Exception as e:
#         print(repr(e))

# RUN
bot.polling(none_stop=True)