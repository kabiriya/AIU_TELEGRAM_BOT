# -*- coding: utf-8 -*-
import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("Факультеты и специальности")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, <b>{0.first_name}</b>!\n<b>{1.first_name}</b>, это бот, созданный для того, чтобы быть вашим помощником и гидом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Факультеты и специальности":

            #markup = types.InlineKeyboardMarkup(row_width=2)
            #item1 = types.InlineKeyboardButton("Ввести повторно", callback_data='1')
            #item2 = types.InlineKeyboardButton("Связаться по этому вопросу", callback_data='0')

            #markup.add(item1, item2)

            bot.send_message(message.chat.id, 'На данный момент мы работаем над внесением все данных и документаций 😊')
        else:
            bot.send_message(message.chat.id, 'Что вы имеете в виду?')




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id, 'Слушаю вас внимательно 😊')
            elif call.data == '0':
                bot.send_message(call.message.chat.id, 'Пожалуйста свяжитесь с нами о номеру +996 707 66 79 11 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)