import telebot
from telebot import types
import openai
import os
import json


openai.api_key = 'API_KEY'

token = "TOKEN"

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda _: True)
def text_mes(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message.text,
        temperature = 0.5,
        max_tokens = 1000,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.0,
    )
    bot_sending_mes = response(['choices'][0]['text'])
    bot.send_message(message.chat.id, bot_sending_mes)

bot.polling()