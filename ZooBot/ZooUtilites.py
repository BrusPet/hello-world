import codecs
from ZooConfig import Questions


def answer_code(answer):
    s = codecs.open('Text.txt', 'r', 'utf-8')
    sign = str(answer[0]) + str(answer[-1])
    an_sum = answer[1] + answer[2]
    if an_sum <= 3:
        an_sum = '3'
    elif an_sum > 3:
        an_sum = '6'
    for i in s:
        if sign == i[0:2]:
            if an_sum == i[2]:
                code = i.split(';')
                return code


def BotException(message):
    if message == 'Начать тест':
        return True
    for value in Questions.values():
        if message in value:
            return True
    else:
        return False

