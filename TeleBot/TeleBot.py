import telebot
from BotConfig import TOKEN, keys
from BotUtilis import ExchangeConverter, ConvertionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ("Чтобы начать работу введите команду боту в формате:\n<валюта> \ <в какую перевести> \ <количество переводимой валюты>"
            "\nВсе доступные валюты: /values")
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступны валюты:"
    for i in keys.keys():
        text = '\n'.join((text, i, ))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def converter(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров')
        if len(values) < 3:
            raise ConvertionException('Слишком мало параметров')

        quote, base, amount = values
        value = ExchangeConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(massage, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'{amount} {keys[quote]} равны {float(amount)*float(value)} {keys[base]}'
        bot.send_message(massage.chat.id, text)


bot.polling()