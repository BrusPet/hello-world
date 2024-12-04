import codecs


TOKEN = '7450162403:AAEupRNXhjdibwieEgGnAEjaWDL1V7IjJj4'

f = codecs.open('Валюта.txt', 'r', 'utf-8')
s = f.readlines()
a = []
keys = {}
for i in s:
        a += i.split()
keys = {a[i]: a[i+1] for i in range(0, len(a) - 1, 2)}

