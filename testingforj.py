from constans import *

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'], regexp='/start')
@bot.message_handler(regexp='/start')
def send_welcome(message):
    msg = bot.reply_to(message, """\
Привет, как тебя зовут?
""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        
        chat_id = message.chat.id
        name = str(message.text)
        if len(name) <3 or len(name)>20:
            msg = bot.reply_to(message, 'Имя должно быть длинее 2 и меньше 20. Повторите попытку ввода')
            bot.register_next_step_handler(msg, process_name_step)
            return
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Сколько лет?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Возвраст должен быть цифрой. Повторите попытку')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        
        msg = bot.reply_to(message, 'Какой пол?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Мужской') or (sex == u'Женский'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, '\n Пол:' + user.sex)
        bots_function(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(regexp="Функции бота")
def bots_function(message):
    
    chat_id = message.chat.id
    g = message.text
    user = user_dict[chat_id] 
    bot.send_message(chat_id, f'Nice to meet you {user.name} \n Age: {user.age} \n Sex: {user.sex}', reply_markup=markup_for_function )

@bot.message_handler(regexp="Настройки")
def bots_setting(message):
    chat_id = message.chat.id
    bot.send_message(chat_id , 'Nice to meet you ', reply_markup=markup_for_setting)

@bot.message_handler(regexp="Изменить имя")
def get_new_name(message):
    msg = bot.reply_to(message,  "Какое имя?")
    bot.register_next_step_handler(msg, new_name)
    
def new_name(message):
    chat_id = message.chat.id
    text = message.text
    
    if (text == u"Изменить имя"):
        get_new_name(message)
    elif (text == u"Изменить возраст"):
        get_new_age(message)
    elif (text == u"Изменить пол"):
        get_new_sex(message)
    elif (text == u"Назад"):
        bots_function(message)(message)
    else:
        name = str(text)
        if len(name) <3 or len(name)>20:
            msg = bot.reply_to(message, 'Имя должно быть длинее 2 и меньше 20. Повторите попытку ввода')
            bot.register_next_step_handler(msg, new_name)
            return
        #user = User(name)
        user = user_dict[chat_id] 
        user.name = name
        bot.send_message(chat_id, 'Nice to meet you ' + user.name )




@bot.message_handler(regexp="Изменить возраст")
def get_new_age(message):
    msg = bot.reply_to(message, 'Повторите ввод возраста')
    bot.register_next_step_handler(msg,new_age)

def new_age(message):
    
    chat_id = message.chat.id
    age = message.text
    
    
    if (age ==  u"Изменить имя"):
        get_new_name(message)
    elif (age ==  u"Изменить возраст"):
        get_new_age(message)
    elif (age ==  u"Изменить пол"):
        get_new_sex(message)
    elif (age ==  u"Назад"):
        bots_function(message)
              
    else:
        age = str(age)
        if not age.isdigit():
            msg = bot.reply_to(message, 'Возраст должен быть цифрой. Повторите попытку?')
            bot.register_next_step_handler(msg, new_age)
            return
        user = user_dict[chat_id] 
        user.age = age
        

        bot.send_message(chat_id, f'Так тебе '+ user.age)


@bot.message_handler(regexp="Изменить пол")
def get_new_sex(message):
 
    msg = bot.reply_to(message, 'Так какой пол', reply_markup=markup_for_sex)
    bot.register_next_step_handler(msg, new_sex)

def new_sex(message):
    chat_id = message.chat.id
    text = message.text
    if (text ==  u'Назад в настройки'):
        bots_setting(message)
        return
    if (text ==  u'Назад в функции'):
        bots_function(message)
        return
    
    if (text == u'Мужской') or (text== u'Женский'):
        sex =  text
        #user = User(sex)
        user = user_dict[chat_id]
        user.sex = sex
    bot.send_message(chat_id, f' \n Пол: {user.sex}' )
    #bots_function(message)


@bot.message_handler(regexp="Назад")
def go_to_settings(message):
    bots_function(message)





if __name__ == '__main__':

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers(delay=6)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()

    bot.polling(none_stop=True)