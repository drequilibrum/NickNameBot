#!/usr/bin/env python
# coding: utf-8

# In[14]:


import telebot
import numpy as np
from keras.models import load_model
import time
import string
from mapping import charId, idChar
characters = list(charId.keys())[1:]
nick_generator = load_model('nick_generator.h5')
TOKEN = 'USE OUR BOT TOKEN HERE'


# In[19]:


symbols = set(characters) - set(string.ascii_letters).intersection(set(characters)) - set([str(i) for i in range(10)]) - set([' '])
markup = telebot.types.ReplyKeyboardMarkup()
for char in symbols:
    markup.add(telebot.types.KeyboardButton(char))


# In[16]:


bot = telebot.TeleBot(token = TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, please provide starting character for a nickname')
    bot.send_message(message.chat.id, "Choose a starting letter, number or one of the following characters:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def return_nicks(message):
    #generated_names = []
    bot.send_message(message.chat.id, 'Following names were generated: ')
    for i in range(10):
        bot.send_message(message.chat.id, gn.generate_name(nick_generator, message.text))
        time.sleep(0.1)
bot.polling()

