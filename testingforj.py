import telebot
from telebot import *
import requests

url = "https://api.telegram.org/bot1032107096:AAHIJN5w49DL0xYaKpOo6YQ6ZO0MOvweOeg/"



bot = telebot.TeleBot('1032107096:AAHIJN5w49DL0xYaKpOo6YQ6ZO0MOvweOeg')
name = ''
surname = ''
age = 0
stut = True
@bot.message_handler(commands=['start'])
def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Your message goes here')



def start(message):
    
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Как тебя зовут?",  reply_markup = hide_markup)
    bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name

def start_after_correction(message):
    
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Как тебя зовут?",  reply_markup = hide_markup)
    bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
def get_name(message): #получаем фамилию
    global name
    name = str(message.text)
    len_name = (len (name))
    hide_markup = telebot.types.ReplyKeyboardRemove()
    if len_name  < 2 or len_name > 20:
        bot.send_message(message.from_user.id, 'Имя должно быть от 2 до 20 символов и не пустым. Введите свое имя еще раз',  reply_markup = hide_markup)
        bot.register_next_step_handler(message,get_name)
      #  return start(message)
    else: 
        bot.send_message(message.from_user.id, 'Сколько тебе лет?',  reply_markup = hide_markup)
        bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    hide_markup = telebot.types.ReplyKeyboardRemove()
    age = message.text #проверяем, что возраст введен корректно
    print (type(age))
    try:
        age = int(age)
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Женщина', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Мужчина', callback_data='no')
        keyboard.add(key_no)
        question = 'Твой пол?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except:
        bot.send_message(message.from_user.id, 'Возраст должен быть написан цифрами. Повторите пожалуйста попытку',  reply_markup = hide_markup)
        bot.register_next_step_handler(message,get_age)

    
def bots_function(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Настройки', 'Функции бота')
    bot.send_message(message.from_user.id, f'Привет {name} tebe {age} ty {stut}', reply_markup=user_markup)
    bot.send_message(message.from_user.id, """Functions of bot """, reply_markup= user_markup)
def bo_set(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')
    bot.send_message(message.from_user.id, 'Напиши свои изменения', reply_markup=user_markup)
    bot.register_next_step_handler(message, handle_text)

def up_name(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')
    
    if  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'назад':
        return bots_function(message)
    else:
        bot.send_message(message.from_user.id, "Как тебя зовут?",  reply_markup = user_markup)
        bot.register_next_step_handler(message, get_update_name) #следующий шаг – функция get_name

def get_update_name (message):
    global name
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')
    
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'назад':
        return bots_function(message)
    else:
        name = str(message.text)
        len_name = (len (name))
        if len_name  < 2 or len_name > 20:
            bot.send_message(message.from_user.id, 'Имя должно быть от 2 до 20 символов и не пустым. Введите свое имя еще раз')
            bot.register_next_step_handler(message,get_update_name)
        else:
            bot.send_message(message.from_user.id, f'Привет {name}')
            bot.register_next_step_handler(message, up_age)

def up_age(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')
    
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'назад':
        return bots_function(message)
    else:
        bot.send_message(message.from_user.id, "Сколько тебе лет?",  reply_markup = user_markup)
        bot.register_next_step_handler(message, get_update_age) #следующий шаг – функция get_name
def get_update_age (message):
    global age
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')

     
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'назад':
        return bots_function(message)
    else:
        try:
            age = int(age)
            age = message.text
            bot.send_message(message.from_user.id, f'возраст: {age}')
            bot.register_next_step_handler(message, up_stut)
        except:
            bot.send_message(message.from_user.id, 'Возраст должен быть написан цифрами. Повторите пожалуйста попытку')
            bot.register_next_step_handler(message,get_update_age)


def up_stut(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Изменить имя', 'Изменить возраст', 'Изменить пол')
    user_markup.row('назад')
    
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'назад':
        return bots_function(message)
    else:
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes= types.InlineKeyboardButton(text='Женщина', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Мужчина', callback_data='no')
        keyboard.add(key_no)
        question = 'Хочепшь изменить свой пол?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global stut
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Настройки', 'Функции бота')
    if call.data == "yes": 
        stut = True
        stut = "Женщина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', reply_markup=user_markup)
    if call.data == "no":
        stut = False
        stut = "Мужчина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', reply_markup=user_markup)
    if call.data == "Zh": 
        stut = True
        stut = "Женщина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', reply_markup=user_markup)
    if call.data == "M":
        stut = False
        stut = "Мужчина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', reply_markup=user_markup)



    


    


@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == 'Настройки':
        return bo_set(message)
    if  message.text == 'Функции бота':
        return bots_function(message)
    if message.text == 'Изменить имя':
        return up_name(message)
    if  message.text == 'Изменить возраст':
        return up_age(message)
    if  message.text == 'Изменить пол':
        return up_stut(message)
    if  message.text == 'назад':
        return bots_function(message)
    



if __name__ == '__main__':
    bot.polling(none_stop=True)

