import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.token)

HIDE_MARKUP = telebot.types.ReplyKeyboardRemove()
KEYBOARD = types.InlineKeyboardMarkup()
KEY_YES = types.InlineKeyboardButton(text='Женщина', callback_data='yes') #кнопка «Да»
KEYBOARD.add(KEY_YES) #добавляем кнопку в клавиатуру
KEY_NO= types.InlineKeyboardButton(text='Мужчина', callback_data='no')
KEYBOARD.add(KEY_NO)
QUESTION = 'Твой пол?'
USER_MARKUP = telebot.types.ReplyKeyboardMarkup()
USER_MARKUP_FOR_SETTINGS = telebot.types.ReplyKeyboardMarkup()
USER_MARKUP_FOR_SETTINGS.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
USER_MARKUP_FOR_SETTINGS.row('Назад')
USER_MARKUP.row('Настройки', 'Функции бота')
name = ''
age = 0
stut = ''

