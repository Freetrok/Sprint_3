import random as r

def gen_login():
    text = 'Sergey_Bogomolov_11'
    random = r.randint(100, 999)
    return f'{text}_{random}@yandex.ru'

log = gen_login()

def gen_pass():
    return r.randint(100000, 999999)

passw = gen_pass()

