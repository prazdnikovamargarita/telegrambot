import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.token)

HIDE_MARKUP = telebot.types.ReplyKeyboardRemove()
markup_for_function = types.ReplyKeyboardMarkup(one_time_keyboard=True,  resize_keyboard=True,row_width=2 )
markup_for_function.add('Настройки', 'Функции бота')

markup_for_setting = types.ReplyKeyboardMarkup(one_time_keyboard=True,  resize_keyboard=True)
markup_for_setting.add('Изменить имя', 'Изменить возраст', 'Изменить пол')
markup_for_setting.add('Назад')


markup_for_sex = types.ReplyKeyboardMarkup(one_time_keyboard=True,  resize_keyboard=True)
markup_for_sex.add('Мужской', 'Женский')
markup_for_sex.add('Назад')

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,  resize_keyboard=True,row_width=2 )
markup.add('Мужской', 'Женский')