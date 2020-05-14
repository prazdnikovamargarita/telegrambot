from constans import *

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?",  reply_markup = HIDE_MARKUP)
    bot.register_next_step_handler(message, get_name) 

def get_name(message): 
    global name
    name = str(message.text)
    len_name = (len (name))
    if len_name  < 2 or len_name > 20:
        bot.send_message(message.from_user.id, '''Имя должно быть от 2 до 20 символов и не пустым.
                                                Введите свое имя еще раз''',  reply_markup = HIDE_MARKUP)
        bot.register_next_step_handler(message,get_name)
    else: 
        bot.send_message(message.from_user.id, 'Сколько тебе лет?',  reply_markup = HIDE_MARKUP)
        bot.register_next_step_handler(message, get_age)
        return name

def get_age(message):
    handle_text(message)
    global age
    age = message.text #проверяем, что возраст введен корректно
    if age.isdigit():
        bot.send_message(message.from_user.id, text=QUESTION, reply_markup=KEYBOARD)
        return age
    else:
        bot.send_message(message.from_user.id, '''Возраст должен быть написан цифрами. 
                                    Повторите пожалуйста попытку''',  
                                    reply_markup = HIDE_MARKUP)
        bot.register_next_step_handler(message,get_age)


def bots_function(message):
    bot.send_message(message.from_user.id, f'Привет {name} ты {age} тебе {stut}',
                                                reply_markup=USER_MARKUP)
    bot.send_message(message.from_user.id, """Functions of bot """, 
                                                reply_markup= USER_MARKUP)

def bo_set(message):  
    bot.send_message(message.from_user.id, 'Напиши свои изменения', 
                                            reply_markup=USER_MARKUP_FOR_SETTINGS)
    bot.register_next_step_handler(message, handle_text)

def up_name(message):
    
    
    if  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'Назад':
        return bots_function(message)
    else:
        bot.send_message(message.from_user.id, "Как тебя зовут?",  
                                                reply_markup =USER_MARKUP_FOR_SETTINGS)
        bot.register_next_step_handler(message, get_update_name) #следующий шаг – функция get_name

def get_update_name (message):
    global name
    name = str(message.text)
    len_name = (len (name))
    if len_name  < 2 or len_name > 20:
        bot.send_message(message.from_user.id, '''Имя должно быть от 2 до 20 символов и не пустым. 
                                        Введите свое имя еще раз''')
        bot.register_next_step_handler(message,get_update_name)
    else:
        bot.register_next_step_handler(message, up_age)

def up_age(message):
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'Назад':
        return bots_function(message)
    else:
        bot.send_message(message.from_user.id, "Сколько тебе лет?",  
                                                reply_markup = USER_MARKUP_FOR_SETTINGS)
        bot.register_next_step_handler(message, get_update_age) #следующий шаг – функция get_name

def get_update_age (message):
    handle_text(message)
    global age
    age = message.text
    if  message.text == 'Изменить возраст':
            return up_age(message)
    elif  message.text == 'Изменить пол':
        return up_stut(message)
    elif  message.text == 'Назад':
        return bots_function(message)
    else:
        if age.isdigit():
            bot.register_next_step_handler(message, up_stut)
        else:
            bot.send_message(message.from_user.id, '''Возраст должен быть написан цифрами. 
                                        Повторите пожалуйста попытку''')
            bot.register_next_step_handler(message,get_update_age)


def up_stut(message):
    if message.text == 'Изменить имя':
        return up_name(message)
    elif  message.text == 'Изменить возраст':
        return up_age(message)
    elif  message.text == 'Назад':
        return bots_function(message)
    else:
        bot.send_message(message.from_user.id, text=QUESTION, reply_markup=KEYBOARD)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global stut
    if call.data == "yes": 
        stut = True
        stut = "Женщина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', 
                                                reply_markup=USER_MARKUP)
    if call.data == "no":
        stut = False
        stut = "Мужчина"
        bot.send_message(call.message.chat.id, f'Привет {name} ты {age} тебе {stut}', 
                                                reply_markup=USER_MARKUP)
    return stut

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
    if  message.text == 'Назад':
        return bots_function(message)
    

    

if __name__ == '__main__':
    bot.polling(none_stop=True)