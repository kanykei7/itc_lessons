# language={
#     'polka':{
#         'name':'python',
#         'version':3.8,
#     },
#     'name':'php',
#     'version':1.9,
# }
# print(language)


# dict2=dict(name='name',age='age',height='height')
# print(dict2)


# person={
#     'name':'John Smith',
#     'age':30,
#     'profession':'python dev'
# }
# person['height']=180#добавление нового ключа и значения
# person['age']=50#изменение значения ключа

# person2={'race':'ork'}
# person.update(person2)


# person.pop('age')#удаляет по ключу
# print(person.get('name'))#обращение к определенному ключу
# print(person)
# print(person['name'])#обращение к определенному ключу
# person.clear()#очищает словарь
# a=person.copy()#копирует словарь
# person.setdefault(7, 'seven')#добавление ключа и его значения но не может изменять существующий

# print(person.values())#посмотреть значения
# print(person.keys())#посмотреть ключи
# print(person.items())#выводит в тюплах пару ключ-значение


# first_dict={}
# first_dict['one']=1
# first_dict['name']='kanykey'
# first_dict['age']=18
# first_dict['height']=165
# first_dict['adress']='manasa,30'
# dict_2={'weight':50,'phone':776849662,'hobby':'python'}
# first_dict.update(dict_2)
# first_dict.pop('one')
# a=first_dict.get('name')
# b=first_dict.copy()
# b['dog']='cat'
# b.setdefault('frog','horse')
# print(b.items())
# print(len(b))
# print(first_dict)
# print(a)

# for key in person:
#     print(key)

# for values in person.values():
#     print(values)


# for key, value in person.items():
#     print(f'{key} = {value}')



# for key in person:
#     if key=='name':
#         person['name']='Will SMith'
#     elif key=='age':
#         person['age']+=18
# print(person)


# a=set()
# b=10
# c='12'
# d=True
# a.add(b)
# a.add(c)
# a.add(d)
# print(a)


# set_1={1,2,3,4,4,4,5,6,7,8}
# print(set_1)


# set1={'arsen','mars','bob','john','almaz','beka'}
# set2={'arsen','mars','bob','abay','manas','josif'}
# set3=set1.difference(set2)#находит недостающие элементы
# print(set3)


# a={1,2,3}
# b={4,5,6}
# a.update(b)
# a.remove(1)
# print(a)


# a={1,2,3,4,5}
# b={1,2,3,7,8,9}
# c=a.intersection(b)#выводит похожие элементы
# print(c)

# a={
#     'number':[4,7,8]
# }

# for value in a.values():
#     print(value[0])


# # Множество № 1:
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6,7}
# dates_of_birth.remove(7)
# print(dates_of_birth)

 
# # Список № 2
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
 
# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a=farm_1.intersection(farm_2)
# a=farm_2.difference(farm_1)
# print(a)
 
# # Словарь №1:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

# a={'drinks':['Coca-Cola','Sprite','Fanta']}
# menu.update(a)
# menu['drinks']=['Coca-Cola','Sprite','Fanta']
# print(menu)


# menu['besh_barmak']=130
# menu['lagman']=135
# menu.pop('borsh')
# print(menu)


# set_1={'cow','monkey','bob',232,'lol'}
# set_1.add('horse')
# set_1.pop()
# print(set_1)


# set_1={'add','udate','intersection','remove','difference','intersection_update','clear','discard','pop'}
# set_2={'clear','get','keys','values','items','update','tuple','set','list','dict'}
# a=set_2.intersection(set_1)
# print(a)



# a={}
# for i in range(3):
#     b=input('name:\n>>')
#     c=input('password:\n>>')
#     a[b]=c
#     print('saved!')
# print(a)    


# a={
#     'kani':'python developer',
#     'eliza':'doctor',
#     'azamat':'football player',
#     'saida':'teacher',
#     'nurbek':'busines'
# }
# for key, value in a.items():
#     print(f'Здравствуйте, {key}.Прекрасная профессия {value}!')


# set_1=set()
# for i in range(10):
#     a=int(input('chislo:\n>>'))
#     set_1.add(a)
# set_2=tuple(set_1)
# print(set_2)


# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# set_1=set(south_american_countries)
# print(set_1)

# suitcase=set()
# for i in range(5):
#     a=input('Выбери вещь:\n>>')
#     suitcase.add(a)
# suitcase.pop()
# print(suitcase)


# suitcase=[]
# while len(suitcase)!=5:
#     a=input('Выбери вещь:\n>>')
#     suitcase.append(a)
# suitcase.pop(4)
# print(suitcase)


# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3=farm_2.intersection(farm_1)
# print(farm_3)


# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”

# ПРИМЕР:
# Дано -> 
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# Результат -> a = Bye
# b = Hi

# for key, value in dict1.items():
#     if value%3==0:
#         print(f'{key}={value} делится без ост на 3')
#     if value%5==0:
#         print(f'{key}={value} делится без ост на 5')
#     else:
#         print('net')




# 2 {'max_word': 'Землю.\n'}
# text = '''
#В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера».
#Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты,
#где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности.
#В 1965 году результат был уже лучше — 24 000 км.
#Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении,
#что использовали при построении следующих аппаратов.
#Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году.
#А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.
# '''

# Напишите программу, которая берёт текст и выводит два слова:
# 1.Наиболее часто встречающееся
# 2.Cамое длинное


# 3 Слияние словарей
# Напишите программу для слияния нескольких словарей в один.





# my_friends = {
#     "Joomart": "+996555246810",
#     "Adinai": "+996555013579",
#     "Ermek": "+996777013579",
#     "Atai": "+996777246810",
#     "Aslan": "+996999246810",
# }

# his_her_friends = {
#     "Lyazat": "+996551123456",
#     "Salavat": "+996552234567",
#     "Daniyar": "+996553345678",
#     "Bolot": "+996554456789",
#     "Alymbek": "+996555501234",
#     "Dastan": "+996556678912",
#     "Maksat": "+996557789012",
#     "Aibek": "+996558890123",
# }
# my_friends.update(his_her_friends)
# print(my_friends)












users = {
    'Admin':{
        'name':'admin',
        'phone':'996555444333',
        'balance':500000,
        'password':'12312321'
    },
    'Argen':{
        'name':'Argen',
        'phone':'999580780',
        'balance':5000,
        'password':'12312321'
    }
}
key = None
while True:
    if key is None:
        print('Здраствуйте уважаемый клиент!')
        m = int(input('''
        1 Заарегистрироваться 
        2 Авторизоваться 
        3 Перевод баланса
        4 Список пользователей 
        5 Информатция 
        6 Выход из банка
        >>> '''))
        if m == 1:
            login = input('введите логин ')
            name = input('введите полное ваше имя ')
            phone = int(input('введите ваш номер +996'))
            password = input('Придумайте пароль ')
            password1 = input('Подтвердите пароль ')
            while password != password1 and len(password) < 8:
                password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
                password1 = input('Повторите пароль ')
            else:
                users.update({
                    login :{
                        'name':name,
                        'phone':phone,
                        'balance':1000,
                        'password':password
                    }
                })
                print('Регистратция успешна')
                key = login
        if m == 2:    
            if key is None:
                print('Добро пожаловать в авторизатцию ')
                login = input('Введите логин ')
                password = input('введите пароль ')
                if login in users:
                    if password == users[login]['password']:
                        print('Вы авторизовались ')
                        key = login
                    else:
                        print('Не верный пароль')
                else:
                    print('Нет такого пользователя ')
            else:
                print('Вы уже авторизованы ')
        if m == 3:
            if users is not None:
                loginP = input('Введите имя получателя ')
                summa = int(input('введите сумму перевода '))
                if loginP in users:
                    if summa <= users[key]['balance']:
                        users[key]['balance'] -= summa
                        users[loginP]['balance']+= summa
                        print('Перевод успешен')
                    else:
                        print('У вас не достаточно денег')
                else:
                    print('такого пользователя нет')
            else:
                print('вы не авторизованы')
        if m == 4:
            if key is not None:
                print(users)
        if m == 5:
            if key is not None:
                print(f'''
                Логин: {users["Admin"]}
                Имя: {users["Admin"]['name']}
                Номер телефона: {users["Admin"]['phone']}
                Баланс: {users["Admin"]['balance']}
                ''')
        if m == 6:
            print('Приходите ещё ')
            break




# d={
#     '1':3,
#     'true': True,
#     'list':[1,2,3],
#     'name':{
#         'bob marley':+7743883,
#         'nicky romero':+993438,
#         'ricky whittle':+555904,
#     }
# }
# print(d['name']['bob marley'])
# print(d['name']['ricky whittle'])


    
# from pprint import pprint
# a={}
# inn =input('введите inn: ')
# id =input('введите id: ')
# year =input('введите year: ')
# gender =input('введите gender: ')
# last_name =input('введите last_name: ')
# name =input('введите name: ')
# status =input('введите status: ')

# a[inn]={
#     'ID':id,
#     'year':year,
#     'gender':gender,
#     'last_name':last_name,
#     'name':name,
#     'status':status
# }
# pprint(a)





