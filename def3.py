
# def func1(a,b):
#     return a+b
# # print(func(5,5))

# c='hello, my name is kanykey'
# def func2(c):
#     count=0
#     for i in c:
#         count+=1
#     return count
# # print(func(a))

# def func3(d,f):
#     if d%2==0 and f%2==0 or d%2!=0 and f%2!=0:
#         return True
#     else:
#         return False
# # print(func(6,6))

# j='привет'
# def func4(j):
#     b='аяуюоеёэиы'
#     count=0
#     for i in j:
#         if i in b:
#             count+=1
#     return count
# # print(func(a))


# password1=input('>>')
# password2=input('>>')
# def func5(password1,password2):
#     if password1==password2 and len(password1)>=8:
#         return 'DONE!'
#     else:
#         return 'NO'
# # print(func(password1,password2))



# def func6():
#     print(func1(5,5))
#     print(func2(c))
#     print(func3(6,6))
#     print(func4(j))
#     print(func5(password1,password2)) 
# print(func6())



# def solution(string):
#     return string[::-1]
# print(solution('hello'))

# def validate_usr(username):
#     a='1234567890'
#     if username!=username.lower():
#         for i in username:
#             if i not in a:
#                 return 'no'
#     else:
#         return 'yes'

# print(validate_usr('jsash'))


# def func1(a,b,c=10):
    # return a+b+c
# print(func1(5,5))
# def square(x):
#     return x**2
# print(square(69))

# from random import choice
# from os import system
# from string import ascii_letters

# def sozdatel(x):
#     for i in range(x):
#         file_name = ''
#         while len(file_name) < 6:
#             file_name += choice(ascii_letters)
#         system(f'touch {file_name}.txt')
# sozdatel(10)



# from cgitb import text
# import os


# def polindrom(x):
#     if x != x[::-1]:
#         return False
#     else:
#         return True

# print(polindrom(''))

# x = 'hello'
# print(x)
# print(x[::-1])



# a =[56,8,9,45,233,5,4,1,0]
# def sorts(x):
#     x.sort()
#     text =" "
#     for i in x :
#         text += str(i)
#         text += ''
#     return text
# print(sorts(a))

# def hello(name,muvi):
#     print(f'привет {name}')
#     print(f'отличный фильм {muvi}')

# hello ('искендер','атака титанов')
# hello ('баель','актан акылый') 
#     

# def name(text):
#     text = f'<h1> {text} </h1>'
#     return text
# print(name('brazzers'))


# def name(text):
#     for i in text:
#         try:
#             int(i)
#         except:
#             return False
#     return True
# print(name('123qw'))

# from os import system
# os.system('ls > files.txt')
# l1=[]
# with open('files.txt', 'r') as f:
#     l=f.read().split()
#     for i in l:
#         if i.endswith('.txt'):
#             os.system(f'rm -rf {i}')
# a=input('>>')
# def func(l):
#     from os import system
#     os.system('ls > files.txt')
#     l1=[]
#     with open(f'files.txt', 'r') as f:
#         files_names=f.read().split()
#         for i in files_names:
#             if i.endswith(l):
#                 os.system(f'rm -rf {i}')
# func(a)



# proverka=['Бишкек','Москва','Астана','Токио','Дели','Шанхай','Сан-Паулу','Мехико','Каир','Мумбаи','Пекин','Дакка','Осак','Армения','Нью Йорк','Карачи','Буэнос Айрес','Чунцин','Стамбул','Калькутта','Манила','Лагос','Тяньцзинь','Киншаса','Гуанчжоу','Лос Анджелес','Москва','Шэньчжэнь','Лахор','Бангалор','Париж','Богота','Джакарта','Ченнай','Лима','Бангкок','Сеул','Нагоя','Хайдарабад','Лондон','Тегеран','Чикаго','Чэнду','Нанкин','Ухань','Хошимин','Луанда','Ахмедабад','Куала Лумпур','Сиань','Гонконг','Дунгуань','Ханчжоу','Фошань','Шэньян','Багдад','Сантьяго','Сурат','Мадрид','Сучжоу','Пуна','Харбин','Хьюстон','Даллас','Торонто','Майами','Сингапур','Филадельфия','Атланта','Фукуока','Хартум','Барселона','Йоханнесбург','Санкт Петербург','Циндао','Далянь','Вашингтон']
# countries=['Бишкек','Москва','Астана','Нью Йорк']


# def add(proverka, countries):
#     country=input('Введите название города:\n>>')
#     if country in countries:
#         return 'Такой город уже есть!', country
#     elif country in proverka:
#         if country not in countries:
#             countries.append(country)
#             return 'Город добавлен!'
#     elif country not in proverka:
#         return 'Некорректное название!'
#     else:
#         return 'что-то пошло не так..'
# print(add(proverka, countries))



























