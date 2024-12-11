import requests
import telebot
from telebot import types
from PIL import Image
from io import BytesIO
from ZooConfig import TOKEN, Questions, Support
from ZooUtilites import BotException, answer_code

bot = telebot.TeleBot(TOKEN)
answers = []
users = {}


@bot.message_handler(commands=['help', ])
def help(message):
    text = ('Для начала теста напишите: Начать тест или используйте команду /start\n'
            'Если хотите оставить отзыв - /feedback\n'
            'Если хотите задать нам вопрос - /support')
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['support', ])
def connect(message):
    bot.send_message(message.chat.id, 'Введите ваше имя:')
    users[message.chat.id] = {}
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    name = message.text
    users['name'] = name
    bot.send_message(message.chat.id, 'Введите ваш email:')
    bot.register_next_step_handler(message, email)


def email(message):
    user_email = message.text
    users['email'] = user_email
    bot.send_message(message.chat.id, 'Какой у вас вопрос?')
    bot.register_next_step_handler(message, question)


def question(message):
    user_question = message.text
    users['question'] = user_question
    bot.send_message(message.chat.id, 'Ваш вопрос принят!\n'
                                      'В ближайшее время вам будет дана обратная связь.')
    text = f'{message.chat.id}' + '\n' + users['name'] + ' ' + users['email'] + ':\n' + users['question']
    bot.send_message(chat_id=Support, text=text)


@bot.message_handler(commands=['feedback', ])
def feedback(message):
    bot.send_message(message.chat.id, 'Введите ваше имя:')
    users[message.chat.id] = {}
    bot.register_next_step_handler(message, user)


def user(message):
    name = message.text
    users['name'] = name
    bot.send_message(message.chat.id, 'Пожалуста, оставьте свой отзыв:')
    print(users)
    bot.register_next_step_handler(message, user_feedback)


def user_feedback(message):
    feed = message.text
    users['feedback'] = feed
    bot.send_message(message.chat.id, 'Спасибо за оставленный отзыв!')
    text = f'{message.chat.id}' + '\n' + users['name'] + ':\n' + users['feedback']
    bot.send_message(chat_id=Support, text=text)


@bot.message_handler(commands=['start', ])
def start(message):
    text = (f'Привествуюем {message.chat.first_name} {message.chat.last_name}.\n'
            f'Добро пожаловать на тест по определению вашего тотемного животного.\n'
            f'<a href="https://moscowzoo.ru/">Московский зоопарк</a> — один из старейших зоопарков Европы. '
            f'Он был открыт 31 января 1864 года по старому стилю и назывался тогда зоосадом.\n'
            f'Московский зоопарк был организован Императорским русским обществом акклиматизации животных и растений.'
            f' Начало его существования связано с замечательными именами профессоров Московского Университета '
            f'Карла Францевича Рулье, Анатолия Петровича Богданова и Сергея Алексеевича Усова.\n\n'
            f'Хотите начать тест?')
    pic = Image.open('Photo/Привет.jpeg')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.InlineKeyboardButton('Начать тест')
    markup.add(item1)
    bot.send_photo(message.chat.id, pic, caption=text, reply_markup=markup, parse_mode='HTML')


@bot.message_handler(func=lambda message: BotException(message.text))
def test(message):
    global answers
    if len(answers) == 4:
        answers = []
    if message.text == 'Начать тест':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton(Questions[f'Q1'][0])
        item2 = types.KeyboardButton(Questions[f'Q1'][1])
        item3 = types.KeyboardButton(Questions[f'Q1'][2])
        item4 = types.KeyboardButton(Questions[f'Q1'][3])
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'Многие животные меняют своё поведение в зависимости от сезона.\n'
                                          f'Пожалуй начнём с этого малого, но очень важного вопроса.\n'
                                          f'Какое у вас любимое время года?', reply_markup=markup)
    if message.text in Questions['Q1']:
        answers.append(Questions['Q1'].index(message.text))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton(Questions[f'Q2'][0])
        item2 = types.KeyboardButton(Questions[f'Q2'][1])
        item3 = types.KeyboardButton(Questions[f'Q2'][2])
        item4 = types.KeyboardButton(Questions[f'Q2'][3])
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'Все мы любим понежиться в теплой кровати, не думая о заботах.\n'
                                          f'Животные в этом так на нас похожи... Или мы на них?\n'
                                          f'Расскажите о вашей активности?', reply_markup=markup)
    if message.text in Questions['Q2']:
        answers.append(Questions['Q2'].index(message.text))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton(Questions[f'Q3'][0])
        item2 = types.KeyboardButton(Questions[f'Q3'][1])
        item3 = types.KeyboardButton(Questions[f'Q3'][2])
        item4 = types.KeyboardButton(Questions[f'Q3'][3])
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'У всех нас разный характер и темперамент.\n'
                                          f'Животные тоже могут сильно отличаться по поведению.\n'
                                          f'Что из перечисленного могло бы вас охарактеризовать?', reply_markup=markup)
    if message.text in Questions['Q3']:
        answers.append(Questions['Q3'].index(message.text))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        item1 = types.KeyboardButton(Questions[f'Q4'][0])
        item2 = types.KeyboardButton(Questions[f'Q4'][1])
        item3 = types.KeyboardButton(Questions[f'Q4'][2])
        item4 = types.KeyboardButton(Questions[f'Q4'][3])
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'Язык и речь - отличительные особенности человека.\n'
                                          f'Но звери тоже умеют общаться.\n'
                                          f'А насколько общительны вы?', reply_markup=markup)
    if message.text in Questions['Q4']:
        answers.append(Questions['Q4'].index(message.text))
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('Показать результат', callback_data='show')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Благодарим вас за уделенное время.\n'
                                          'Тест пройден и ваше тотемное животное уже ждет, хотите узнать результат?',
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'show')
def show(call):
    code = answer_code(answers)
    pic = requests.get(code[3][:-2])
    img = Image.open(BytesIO(pic.content))
    text = f'Ваше тотемное животное - {code[1]}.\n{code[2]}\n'
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Узнать больше', callback_data='ссылка')
    bot_link = (f"http://vk.com/share.php?url=https://t.me/Zoo_Testbot&image={code[3][:-2]}" +
                f"&title=Мое%20тотемное%20животное%20{code[1]}")
    button = types.InlineKeyboardButton("Поделиться результатом ", url=bot_link)
    markup.add(item1, button)
    bot.send_photo(call.message.chat.id, img, caption=text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'ссылка':
            text = ('В рамках Программы лояльности Московского зоопарка любой желающий может взять одно из животных под'
                    ' свою опеку. Все - от маленьких посетителей до больших корпораций, - кто неравнодушен к жизни обит'
                    'ателей зоопарка, может стать участником программы.\n'
                    'Вы всегда можете задать нам вопрос или оставить свой отзыв:\n'
                    '/support - задать вопрос\n'
                    '/feedback - оставить отзыв')
            markup = types.InlineKeyboardMarkup(row_width=2)
            pic = Image.open('Photo/MZoo-logo-hor-rus-preview-RGB.jpg')
            item1 = types.InlineKeyboardButton('Клуб друзей Московского Зоопарка',
                                               url='https://moscowzoo.ru/animals/kinds?class_animals=65359c31f663e25589e58217')
            item2 = types.InlineKeyboardButton('Программа опеки в Московском Зоопарке',
                                               url='https://moscowzoo.ru/about/guardianship')
            button = types.KeyboardButton('Начать тест')
            markup.add(item1, item2)
            bot.send_photo(call.message.chat.id, pic, caption=text, reply_markup=markup, parse_mode='HTML')
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup2.add(button)
            bot.send_message(call.message.chat.id, text='Так же при желании, вы можете пройти тест еще раз',
                             reply_markup=markup2)


bot.polling()
