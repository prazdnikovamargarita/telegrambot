import telebot
from telebot import *
bot = telebot.TeleBot('%1032107096:AAHIJN5w49DL0xYaKpOo6YQ6ZO0MOvweOeg%')
name = ''
surname = ''
age = 0
stut = True


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
   

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text, get_stut) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

def get_stut(message):
    global stut
    age = message.text
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Женщина', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Мужчина', callback_data='no')
    keyboard.add(key_no)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker1(call, message):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(message.from_user.id, f'Привет {name}')
        bot.register_next_step_handler(message, main_menu)
        stut = True
    elif call.data == "no":
        bot.send_message(message.from_user.id, f'Привет {name}')
        bot.register_next_step_handler(message, main_menu)
        stut = False
@bot.message_handler(content_types = ['text'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(True, False)
    markup.row('Настройки', 'Функции бота')
    bot.send_message(message.from_user.id, f'Привет {name}', reply_markup=markup)
    
@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == 'Настройки':
        bot.register_next_step_handler(message, bots_settings)
    if  message.text == 'Функции бота':
        bot.register_next_step_handler(message, bots_function)

def bots_function(message):
    bot.send_message(message.text, 'Настройки бота')
    bot.send_message(message.text, 'Вам понятно?')
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker2(call, message):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(message.from_user.id, 'Отлично ')
        bot.register_next_step_handler(message, main_menu)
    elif call.data == "no":
        bot.send_message(message.from_user.id, 'Прочитай еще раз')
        


@bot.message_handler(content_types = ['text'])
def bots_settings(message):
    bot.register_next_step_handler(message, start)

if __name__ == '__main__':
     bot.polling(none_stop=True)

