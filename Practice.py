# print(f'Таблица умножения:')
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i*j}', end = '\t')
#     print(f'')
# else:
#     print(f'Приложение выполнено успешно.')

# print(f'1 - главный герой - лучник / ДД +++ ')
# print(f'2 - лучник - призыватель / ДД - хил сап +++ ')
# print(f'3 - вроде кинетик - glass cannon ДД')
# print(f'4 - милик с косой ДД / ТАНК +++ ')
# print(f'5 - хз кто-то с магией наверно')
# print(f'6 - хил')
# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))
# s = 'Hello'
# print(s, id(s))
# s += ', World!'
# print(s, id(s))

# list = [1, 2, 3]
# print(list, id(list))
# for i in range(4, 11):
# # #     list.append(i)
# # # print(list, id(list))

# from copy import copy


# print(f'\nЗадание #1:')
# list1 = [1, 2, 3]
# list1copy = copy(list1)
# for i in range(0, len(list1copy)):
#     list1copy[i] = list1copy[i]*2
# print(f'Ответ:\t{list1copy}')
# print(f'\nЗадание #2:')
# sum = 0
# list2 = [1, 2, 3]
# for i in range(0, len(list2)):
#     sum += list2[i]**2
# print(f'Ответ: \tcумма квадратов членов списка: {sum}')
# print(f'\nЗадание #3:')
# list_time = [3, 6.7, 11.8]
# print(f'Ответ:')
# for i in range (0, len(list_time)):
#     print(f'\t{i+1}. Необходимый объем воды при {list_time[i]} часах: {int(list_time[i] // 2)} литра(ов).')
# print(f'\nЗадание #4:')
# s4 = 'Hello world'
# if s4.find(' ') >= 0:
#     print(f'Ответ:\n\t' + s4.upper())
# else:
#     print(f'Ответ:\n\t' + s4.lower())
# print(f'')

# t1 = (1, 2, 3)
# t2 = 1, 2, 3 # упаковка кортежа - не очень желательно так делать
# x, y, z = t2 # распаковка кортежа
# l1 = [1, 2, 3]
# print(type(t1))
# print(type(l1))
# print(type(t2))
# t3 = tuple((1, 2, 3))
# t4 = () # пустой кортеж
# print(type(t3))

# t1 = tuple('Hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# words_r = []
# for i in words:
#     if i == i[::-1]:
#         words_r.append(i)
#     else:
#         continue
# print(words_r)

# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши Молоко']
# new_str = []
# for i in my_str:
#     row_s = i.replace(' ', '').lower()
#     if row_s == row_s[::-1]:
#         new_str.append(i)
#     else:
#         continue
# print(new_str)

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# pali_words = [i for i in words if i == i[::-1]]
# print(pali_words)

# s1 = set(i for i in range(0, 11))
# print(s1)
# s2 = set(s for s in s1)
# print(s2)
# s3 = set() # конструктор пустого множества
# print(type(s3), end = ' ')
# print(s3)

# a = set('abracadbra')
# b = set('alacazam')
# print(a, b, sep = '\n')
# c = a - b # из А убрать символы В
# print(c)
# d = a | b # объединение - ВСЕ символы однократно
# print(d)
# e = a & b # пересечение - ТОЛЬКО дубли
# print(e)
# f = a ^ b # множества из элементов - все символы КРОМЕ дублей
# print(f)
# f.add('dog')
# print(f)
# f.discard('dog')
# print(f)
# f.clear
# print(f)

# a = frozenset('cat') # ннизменяемое множество set

# d = {} # пустой словарь
# print(type(d), end = ' ')
# print(d)

# product_1 = {
#     'brand' : 'Sony',
#     'type'  : 'Phone',
#     'price' : 100,
# }
# print(product_1)

# product_2 = dict(brand='Apple', type='iPhone', price=150)
# print(product_2)

# l_users = [ # с кортежами то же самое
#     ['kmzaha@gmail.com', 'Zahadum'],
#     ['nastya3k@yandex.ru', 'Laorika'],
#     ['kostya@outlook.com', 'Mimiznya']
# ]
# d_users = dict(l_users)
# for k in d_users:
#     print(f'{d_users[k]} \t: {k}')

# product_3 = {i: i + 1 for i in range(1, 11)}
# print(product_3)

# product_1 = {
#     'brand' : 'Sony',
#     'type'  : 'Phone',
#     'price' : 100,
# }
# print(product_1)
# print(product_1['brand'])

# product_2 = dict(brand='Apple', type='iPhone', price=150)
# print(product_2)
# print(product_2.get('type'))
# print(product_2.get('model', 'NOT EXIST'))

# for k in product_2:
#     print(f'{k} :\t\t{product_2[k]}')

# product_1 = {
#     'brand' : 'Sony',
#     'type'  : 'Phone',
#     'price' : 100,
# }
# print(product_1.items())
# for key, value in product_1.items():
#     print(f'{key}\t: {value}')

# products = [
#     {'brand': 'Sony','price': 100},
#     {'brand': 'Apple','price': 150},
#     {'brand': 'Samsung','price': 140}
# ]
# for prod in products:
#     print(prod['brand'], prod['price'], sep = '\t: ')

# z = int(input(f'Введите предел таблицы умножения от 2 до 10: '))
# def get_calc(x, y):
#     return x * y
# for x in range (1, z+1):
#     for y in range (1, z+1):
#         print(f'{x} х {y} = {get_calc(x, y)}', end = ' \t')
#         if y == z:
#             print('')
           
# def space_check(s):
#     if ' ' in s:
#         return s.upper()
#     else:
#         return s.lower()
# print(space_check('Hello World'))
# print(space_check('Hello_World'))

# def get_sum(a=0, b=0, c=0, d=0):
#     full_sum = [a, b, c, d]
#     for i in full_sum:
#          print(f'i = {i}')
#     return a + b + c + d
# print(get_sum(1, 2, 5, 7))
# print(get_sum(6, 8))

# def get_total(*args):
#     return sum(args)
# print(get_total(1, 4, 6, 7, 8, 8, 99, 45, 444))

# a = 22

# def local_1():
#     global a # если нужно поменять global
#     a = 33
#     print(f'a = {a}')

# def local_2():
#     a = 44
#     print(f'a = {a}')
    
# def local_3():
#     a = 55
#     print(f'a = {a}')
    
# local_1()
# local_2()
# local_3()
# print(f'a = {a}')

# print(f'Задание #1:')
# def odd_ball(arr,):
#     return arr.index('odd') in arr
# print(f'Ответ:\t\tПоследовательность №1: ', odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even']))
# print(f'\t\tПоследовательность №2: ', odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even']))
# print(f'\t\tПоследовательность №3: ', odd_ball(['even', 10, 'odd', 2, 'even']))

# print(f'Задание #2:')
# def find_sum(n):
#     return sum(i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0)
# print(f'Ответ:\t\tCумма всех чисел кратных 3 или 5 в списках:', find_sum(5), ' и ', find_sum(10))

# print(f'Задание #3:')
# names = ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul', 'Teddy', 'Alan']
# def get_names(names):
#     return [i for i in names if len(i) == 4]
# names2 = get_names(names)
# print(f'Ответ:\t\t{names2}')

# from random import randint as rand
# from random import shuffle as shuff
# from re import S
# deck = []
# for suit in range (1, 5):
#     for value in range (2, 15):
#         if suit == 1:
#             card_suit = 'S' # SPADES - ПИКИ
#         elif suit == 2:
#             card_suit = 'D' # DIAMONDS - БУБНЫ
#         elif suit == 3:
#             card_suit = 'C' # CLUBS - ТРЕФЫ
#         elif suit == 4:
#             card_suit = 'H' # HEARTS - ЧЕРВИ
#         else:
#             print(f'Unknown card_suit detected!')
#             break
#         if value == 2:
#             card_value = '02'
#         elif value == 3:
#             card_value = '03'
#         elif value == 4:
#             card_value = '04'
#         elif value == 5:
#             card_value = '05'
#         elif value == 6:
#             card_value = '06'
#         elif value == 7:
#             card_value = '07'
#         elif value == 8:
#             card_value = '08'
#         elif value == 9:
#             card_value = '09'
#         elif value == 10:
#             card_value = '10'
#         elif value == 11:
#             card_value = '!J'
#         elif value == 12:
#             card_value = '!Q'
#         elif value == 13:
#             card_value = '!K'
#         elif value == 14:
#             card_value = 'A!'
#         else:
#             print(f'Unknown card_value detected!')
#             break
#         card = [card_suit, card_value]
#         deck.append(card)

# def print_deck(deck):
#     step = 0
#     for i in deck:
#         print(i, end = '\t')
#         step += 1
#         if step % 13 == 0:
#             print('')

# shuff(deck)
# print_deck(deck)

# import libs
# s = 'Hello World!'
# print(libs.get_count(s, 'l'))
# print(libs.get_len(s))

# from datetime import datetime, timedelta
# import locale

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# today = datetime.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())

# now1 = datetime.now()
# now2 = datetime.today()
# print(now1, now2, sep = '\n')
# print(f'{now1.strftime("%A %d %b %Y")}, {now1.strftime("%H:%M")}')
# print(now1.strftime('%c'))
# now3 = now1 + timedelta(days=1, hours=2, minutes=10)
# print(now3.strftime('%c'))


# from libs import read_dir
# read_dir('C:\IT Tools\PyProjects')


# f = open('C:\IT Tools\Test\Test1.txt', 'r', encoding='utf-8') # 'r' - для чтения
# print(f.encoding)
# text1 = f.read()
# print(text1) 
# f.close()
# f = open('C:\IT Tools\Test\Test1.txt', 'a', encoding='utf-8') # 'a' - чтение и запись
# f.write('Новая строка2\n')
# f.close()
# line = ['Супер новая строка 01', 'Супер новая строка 02']
# f = open('C:\IT Tools\Test\Test1.txt', 'a', encoding='utf-8') # 'a' - чтение и запись
# for i in line:  # запись по строкам + \n циклом for
#     f.write(i + '\n')
# f.close()
# f = open('C:\IT Tools\Test\Test1.txt', 'a', encoding='utf-8') # 'a' - чтение и запись
# f.writelines(f'{i}\n' for i in line) # запись по строкам + \n и метод writelines
# f.close()
# f = open('C:\IT Tools\Test\Test1.txt', 'r', encoding='utf-8') # 'r' - для чтения
# for line in f: # чтение по строкам
#     print(line, end = '') # чтобы убрать лишний \n
# f.close()

# for i in range(1, 5):
#     f_a = ('C:\IT Tools\Test\Test' + str(i) + '.txt')
#     lines = ['Вы отккрыли файл по адресу:', f_a, 'Хо Хо Хо!!!']
#     f = open(f_a, 'a', encoding='utf-8') # 'a' - запись и создание при отсутствии
#     f.writelines(f'{i}\n' for i in lines)
#     # print(f'{f_a} - запись(создание + запись) успешно.')
#     f.close()

# while True:
#     try:
#         div = int(input(f'Привет! Введи любое число: '))
#         print(f'100 / {div} = {100 / div}')
#         break # при успешном вполнении выходтим из бесконечного цикла
#     except ZeroDivisionError: # если введен 0, а на 0 делить нельзя
#         print(f'DIVISION TO ZERO ERROR')
#     except ValueError: # если введен текст вместо числа
#         print(f'VALUE TYPE ERROR') 
#     except Exception: # если произошла ошибка
#         print(f'UNKNOWN EXCEPTION ERROR')
#     else: # если все прошло хорошо
#         print(f'Все прошло успешно!')
#     finally: # выполняется в любом случае
#         print(f' ')

# class MyFirstPythonClass:
#     name = 'Костя'
    
#     def say_hi(self, name=''):
#         if name:
#             print(f'Привет, {name}!')
#         else:
#             print(f'Привет, {self.name}!')
        
# a = MyFirstPythonClass()
# a.say_hi()
# a.say_hi('Настя')

# from classes import Person, Employee

# emp01 = Employee('Rick', 56, 'Blizzard')
# emp01.print_info()
# print(emp01.company)
# print(emp01)
# per01 = Person('Greg', 45)
# print(per01)

# def hello():
#     return 'Hello, i\'m [func_hello]'

# def super_func(func):
#     print(f'Hello, i\'m [super_func]')
#     print(func())
    
# def my_decorator(func):
#     def func_wrapper():
#         print(f'Code before:')
#         func()
#         print(f'Code after:')
#     return func_wrapper

# def decorator_test():
#     print(f'Hello I\'m DECORATOR_TEST')

# test = my_decorator(decorator_test)
# test()

# def make_upper(fn):
#     def my_wrapper():
#         title = fn()
#         title = title.upper()
#         title = title.replace(' ', '_')
#         return title
#     return my_wrapper

# @make_upper
# def hi():
#     return f'  Hello World!  '


# print(hi())


# def get_double(my_list):
#     return list(map(lambda num: num * 2, my_list))

# my_123list = [1, 2, 3]
# print(get_double(my_123list))

import re

# s = 'Это просто строка текста. А это просто еще одна строка текста.'
# pattern = 'строка'

# if re.search(pattern, s):
#     print(f'MATCH FOUND!')
# else:
#     print(f'NO MATCHES FOUND!')

# match = re.search(pattern, s)
# print(match)

# print(re.match(pattern, s))

# print(re.findall(pattern, s))

# print(re.split(r'\.', s))
# print(re.split(r'\.', s, 1))

# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''

# pattern = r'\w' # по симворльно буквы, цифры и нижний пробел
# print(re.findall(pattern, s), end = '\n\n')

# pattern = r'\w+' # по словно, цифры и нижний пробел
# print(re.findall(pattern, s), end = '\n\n')

# pattern = r'[Эт]' # по шаблону символов
# print(re.findall(pattern, s), end = '\n\n')

# pattern = r'[а-я]+' # по диапазону букв русского языка + пословно // можно побуквенно
# print(re.findall(pattern, s), end = '\n\n')

# pattern = r'[a-z0-9]' # по диапазону букв английского языка побуквенно и цифры 0 - 9
# print(re.findall(pattern, s), end = '\n\n')

# pattern = r'[а-я]+' # по диапазону букв русского языка + пословно // можно побуквенно
# print(re.findall(pattern, s, flags=re.IGNORECASE), end = '\n\n') # регистронезависимый поиск

# pattern = r'[0-9]+' # числа
# print(re.findall(pattern, s), end = '\n\n')

# def validate_email(mail):
#     return re.match(r'^.+@(\w+\.){0,2}[a-zа-я]{2,6}$', mail, re.IGNORECASE)

# print(validate_email('nastya3k@yandex.ru'))
# print(validate_email('kmzaha@gmail.ru'))
# print(validate_email('мимижня@mail.рф'))
# print(validate_email('mylnikoff@google.com.eu'))
# print(validate_email('mylnikoff@microsoft'))

# def dict_factory(cur, row):
#     d = {}
#     for idx, col in enumerate(cur.description):
#         d[col[0]] = row[idx]
#     return d

# import sqlite3

# database = sqlite3.connect('test_db.s3db')
# database.row_factory = dict_factory
# cursor = database.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)')
# cursor.execute('INSERT INTO USERS (name, email) VALUES ("Ианов Иван", "ivanov@gmail.com")')
# cursor.execute('INSERT INTO USERS (name, email) VALUES ("Петров Петр", "petrov@gmail.com")')
# cursor.execute('INSERT INTO USERS (name, email) VALUES ("Андреев Андрей", "andreev@gmail.com")')
# cursor.execute('INSERT INTO USERS (name, email) VALUES ("Федоров Федор", "fedorov@gmail.com")')
# cursor.executescript('''
# INSERT INTO USERS (name, email) VALUES ("Михайлов Михаил", "mihailov@gmail.com");
# INSERT INTO USERS (name, email) VALUES ("Сергеев Сергей", "sergeev@gmail.com");
# ''')
# database.commit()

# users = [
#     ('user 1', 'user_1@mail.ru'),
#     ('user 2', 'user_2@mail.ru'),
#     ('user 3', 'user_3@mail.ru'),
#     ('user 4', 'user_4@mail.ru')
# ]
# cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)
# database.commit()

# email = 'petrov@gmail.com'
# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'") # будет работать, НО тогда схватишь SQL инъекцию!!! так делать НЕЛЬЗЯ
# cursor.execute("SELECT * FROM users WHERE email = ?", [email]) # уже лучше
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'Сергеев Сергей'}) # вот так!!! надо
# res = cursor.fetchone()
# print(res)
# print(res[1]) #доступ по индексу кортежа

# cursor.execute("SELECT * FROM users")
# res = cursor.fetchall()
# for rec in res: print(rec['name'], rec['email'])
# database.close()

# import zipfile, os

# folder_path = r'C:\IT Tools\Test' # путь к папке
# zip_path = r'C:\IT Tools\Test\test.zip' # путь к файлу
# zip_name = r'test.zip' # имя архива

# my_zip = zipfile.ZipFile(zip_path, 'w')

# for folder, subfolder, file in os.walk(folder_path):
#     for every_file in file:
#         if every_file == zip_name:
#             continue
#         my_zip.write(os.path.join (folder, every_file),
#         os.path.relpath(os.path.join(folder, every_file), folder_path),
#         compress_type=zipfile.ZIP_DEFLATED)

# my_zip.close()

# from tkinter import *
# from tkinter import ttk # кнопки под ОС стиль

# root = Tk() # root - так договорились
# root.config(bg='#FFE4B5') # цвет фона
# root.geometry('900x900+550+50') # размеры и место появления
# root.resizable(False, False) # запрет resize окна по-диагонали и вертикали
# root.title('Очень люблю Настеньку!')
# root.iconbitmap(r'C:\IT Tools\Test\Icons\sunny.ico')

# def btn_clicked():
#     print(f'Push the Button!')

# btn = ttk.Button(root, text=r'OK', command=btn_clicked, width=10) # width - ширина кнопки в символах / 
# btn.pack()

# btn2 = Button(root, text=r'TEST', font=('Comic Sans MS', 24, 'italic'))
# btn2.pack()

# btn3 = Button(root, text=r'QUEST', font=r'Garamond 20 bold').pack() # но иожно и так

# import time
# def check_time():
#     btn_time['text'] = time.strftime(f'%H:%M:%S')
    
# btn_time = Button(root, text=r'Проверка времени', command=check_time)
# btn_time.pack()

# total_cntr = 0
# def cntr():
#     global total_cntr
#     total_cntr +=1
#     root.title(f'Очень люблю Настеньку! {total_cntr}')

# btn_cntr = Button(root, text=r'Счетчик кликов', command=cntr)
# btn_cntr.pack()

# l1 = Label(root, text=f'Строка 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5', bg='#FFE4B5', fg='#000080', font=('Gothic', 20))
# l1.pack()

# image_01 = PhotoImage(file='C:\IT Tools\Test\python_art.png') # работа с картинкой
# l_logo = Label(root, image=image_01)
# l_logo.pack()

# l_label = Label(root, text=r'Поле ввода: ', bg='#FFE4B5')
# l_label.pack()

# e = Entry(root)
# e.insert(0, r'Привет') # добавляем в начало поля
# e.insert(END, r' Солнышко!') # добавляем в конец первой строки
# # e.delete(0, END) # удаляем символы в поле - от начала до конца
# e.pack()

# e_task = Entry(root)
# e_task.pack()

# def text_add():
#     e_task.insert(END, r'Hello!')
    
# def text_clear():
#     e_task.delete(0, END)

# def text_get():
#     l_task['text'] = e_task.get()

# button_get = Button(root, text=r'Add', command=text_add).pack()
# button_add = Button(root, text=r'Clear', command=text_clear).pack()
# button_clr = Button(root, text=r'Get', command=text_get).pack()
# l_task = Label(root, text=f'Здесь будет текст!', bg='#FFE4B5')
# l_task.pack()

# # e_pass = Entry(root, show='*') # выдаст другие символы вместо вводимых - удобно в полях пароля )
# # e_pass.pack()

# root.mainloop()