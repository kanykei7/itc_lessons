# name=input("your name:\n>>")
# text=f'Hello {name}! Its me!!!'
# print(text)


# name=input("your name:\n>>")
# name=name.lower()

# print(name.startswith('a'))
# print(name.endswith('a'))

# if name.lower().startswith('a') and name.endswith('a'):
#     print('vashe imya nachinaetsya na "A" i zakanchivaetsya na "a"')
# else:
#     print('vashe imya ne naschinaetsya na "A"')




# text='world school may'
# print(text.split())

# text1='world,school,may'
# print(text1.split(','))

# text='world school may'#delaet pervye bukvy zaglavnymi
# print(text.title())

# text='      world school may     '#udalyaet lishnie probely
# print(text.strip())

# text='world school may'
# s='|'.join(text)#dobalyaet posle kajdoi bukvy
# print(s)

# text='world school may'
# print(text.count('o'))#kol-vo bukv 

# text='world school may'
# print(text.isalpha())#vozvratit true tolko esli budut tolko bukvy
# print(text.isdigit())#vozvaratit true esli tolko iz cifir




# password=input('your password:\n>>')
# password2=input('repeat password:\n>>')

# print(len(password))

# if password.isalpha() or password.isdigit():
#     print(f'vash parol {password} doljen sostoyat iz bukv i cifir')
# elif len(password)<8:
#     print(f'parol {password} doljen sostoyat iz 8 symbols ili bolee')
# elif password!=password2:
#     print(f'parol ne sovpadaet:\n{password}!={password2}')
# else:
#     print('avtorizaciya proshla uspeshno')


# text='hellt'
# print(text.replace('t','o'))




# a='hello'
# b=' WOld'
# print(a.upper()+b.lower())

# a=True
# print(str(a))

# #Строка №1:
# from curses.ascii import isalpha


# a='Google создаст специальную команду для поиска багов в особо важных приложениях.'
# # #Строка №2:
# b='Integers Floats Strings Lists Tuples'
# # #Строка №3:
# c='хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# # #Строка №4:
# d='GitHub'
# # #Строка №5:
# e='Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
# # #Строка №6:
# f='Самые важные собЫтия в миРе инфосека за сентябрь'
# # #Строка №7:
# g='Прошли те времена, когда компьютер был грязно-белой офисной коробкой.'
# # Строка №8:
# y="У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"


# answer=input('luboi simvol\n>>')
# print(d.split(answer))


# print(e.replace('е','3'))


# name=input('your name\n>>')
# age=input('your age\n>>')
# film=input('your favorite film\n>>')
# print(f'Hello, {name}, i like {film} too')


# k=a.split()
# m=len(k)
# print(m)


# p=('|').join(f)
# print(p)


# print(c.title())


# for i in 'hello world':
#     print(i * 2, end='')



# import random
# while True:
#     num = random.randint(1, 5)
#     print('I picked a number among 1 and 5. Try to guess it!')
#     while True:
#         x = int(input('The number is: '))
#         if x > 5 or x < 1:
#             print('The number can not be more than 100 or less then 1. Try again!')
#             continue
#         elif x > num:
#             print('Wrong one! Try LESS!')
#             continue
#         elif x < num:
#             print('Wrong one! Try MORE!')
#             continue
#         else:
#             choise = input('GOT IT! Want to play again? Type Y or N: ')
#             break
#     if choise == 'Y' or 'y':
#         continue
#     elif choise == 'N' or 'n':
#         print('Ok. Bye bye!')
#         break
#     else:
#         print('wtf bro')
#         break




# password=input('password:\n>>')
# repeat_password=input('repeat password:\n>>')
# if password.isalpha() or password.isdigit():
#     print('Пароль должен состоять из букв и цифр')
# elif len(password)<6:
#     print('Пароль должен состоять из 6 или более символов')
# elif password!=repeat_password:
#     print('Пароль не совпадает!!!\nПовторите попытку')
# else:
#     print('Пароль готов!')


# def m(a,b):
#     return a*b
# print(m(2,2))




user={
    'kanykey':{
        'login':'kani00',
        'password':"qwerty645635"
    }
}
file=open('file.txt', 'w')
log=str(input('вы уже авторизованы?\nyes/no\n>>'))
if log=='yes':
    login=input('введите логин\n>>')
    if login in user['kanykey']['login']:
        password=input('введите пароль\n>>')
        if password in user['kanykey']['password']:
            print('вы вошли в аккаунт')
        else:
            print('Пароль невепы\nПовторите снова')
    else:
        print('логин не совпадает')
elif log=='no':
    new_login=input('Придумайте логин <3\n>>')
    if len(new_login)<4:
        print('Логин должен состоять из 4 или более символов')
        pass
    else:
        print('Отлично')
        print('Придумайте пароль <3\nПароль должен состоять из букв и цифр')
        password=input('password:\n>>')
        repeat_password=input('repeat password:\n>>')
        if password.isalpha() or password.isdigit():
            print('Пароль должен состоять из букв и цифр')
        elif len(password)<6:
            print('Пароль должен состоять из 6 или более символов')
        elif password!=repeat_password:
            print('Пароль не совпадает!!!\nПовторите попытку')
        else:
            with open('file.txt', 'a+') as file:
                file.write(new_login)
                file.write(password)
                user_list = []

            with open('file.txt', 'a+') as file:
                for line in file:
                    user_list.append()
            print(f'Пароль сохранен <3\nВаш логин:{new_login}\nВаш пароль:{password}')




# user_data = input()
# with open('file.txt', 'a+') as file:
#     file.write(user_data)
#     user_data_list = []

# with open('file.txt', 'r') as file:
#     for line in file:
#         user_data_list.append(line)

# user_data = user_data_list['x']