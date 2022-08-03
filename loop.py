# a=['kani','azamat','almaz','john','bektur','kanat','bob','akyl','bermet','asel']
# for i in a:
#     if i == 'azamat':
#         print('da gudda')
#     else:
#         print('такого слова нет')


# a=[1,2,3,4,4,4,5,6,7,8,9]
# count=0
# for i in a:
#     if i==4:
#         count+=1
# print(count)



for i in range(1,10+1):
    # a=i*5
    print(i)



# a=[]
# b=int(input('chislo:\n>>'))
# for i in range(b+1):
#     a.append(i)
#     print(a)



# for i in range(1,10+1):
#     b=5
#     c=b*i
#     print(f'{b} * {i} = {c}')


# b=int(input(''))
# a=['bishkek', 'piter', 'moscow', 'naryn', 'osh','batken']
# for i in range(len(a)):
#     if b == i:
#         print(a[i])


# a=['bishkek', 'piter', 'moscow', 'naryn', 'osh','batken']
# for i in a:
#     if i=='osh':
#         a.remove('osh')
# print(a)




# i=0
# while i<10:
#     i+=1
#     print(i)


# count=0
# a=int(input(''))
# while a != 0:
#     print('repeat')
#     count+=1
#     a=int(input())
# print(f'вы потратили {count} попыток')


# a=[1,2,3]*5
# while 3 in a:
#     a.remove(3)
#     print(a)


# a = ['azamat', 'bektur', 'ilgiz', 'nikita', 'joma', 'arsen']
# for i in a:
#     if i == 'nikita':
#         continue
#     print(i, end=', ')




# 1. Допустим у нас есть список языков программирования. 
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#  Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
#  Если этого языка нет в списке, ничего не нужно выводить.

# for i in languages:
#     if lang1 in languages:
#         print('this languages is in list')



# 2. Будем работать с тем же списком: 
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, цикл должен быть прерван.
# for i in languages:
#     if i=='php':
#         break
#     print(i)




#  3. Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз. 
# for i in range(7):
#     i*=5
#     print(i)

# 4. Напишите код, который выведет на экран список языков с нумерацией.



# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# Вывод:
#  0 go
#  1 java
#  2 php
#  3 python
#  4 javascript
#  5 ruby
# for i in enumerate(languages):
#     print(i)
    



# 5. Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиление:
# Получите такой же результат но с ОДНИМ циклом

# for i in range(0,10):
#     print(i)
# for i in range (0,10):
    

#  6. У вас есть список имён: 
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#   Если первое имя = 0, второе имя = 1 и т.д.
#  Выведите на экран всё имена которые лежат на чётных числах
# for i in names:
#     b=names[::2]
# print(b)



# 7. У вас всё тот же список имён:
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
#  Выведите каждое 2 имя.
#  Подсказка: Всего имён 13.


# for i in names:
#     b=names[1::2]
# print(b)

# 8. Есть переменная которая хранит в себе число:
#  Необходимо написать следующие условия для проверки переменной:
#     1. Это число трёхзначное?
#      2. Это число положительное и чётное?
#     3. Это число делится на 31 без остатка?
#    4. Если это число больше 100 и оно делится на 17 без остатка или это число 
# больше 150 и равно 13**2 тогда показать что это за число

# a=1234
# if a>99:
#     print('trehzhach')
# else:
#     print('net')
# if a>=0 and a%2==0:
#     print('polojit i chetnoe')
# else:
#     print('net')
# if a%31==0:
#     print('delitsa na 31 bez ost')       
# else:
#     print('net')
# if a>100 and a%17==0 or a>150 and a==13**2:
#     print(a)
# else:
#     print('net')

# 9. Сгенерировать 200 чисел от -100 до 100:
#   1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
#   2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
#   3. Посчитать сколько чисел подходят под первое условие
#   4. Посчитать сколько чисел подходят под второе условие
  
# count=0
# for i in range(-100,100):
#     if i % 13==0 and i%2==0:
#         b=i**2
#         count=count+1
#         print(b)
# print("kol-vo", count)


# count=0
# for i in range(-100,100,7):
#     if i%2!=0:
#         print(i)
#         count=count+1
# print('kol-vo', count)











# a = ['Bish', 'osh', 'batken','karakol', 'kant', 'naryn', 'talas']
# while True:
#     command = input('''Выберите действие: 
#     > Добавить 
#     > Отобразить
#     > Заменить 
#     > Удалить 
#     > Выход
#     > ''')
#     if command == 'добавить':
#         add = input('Добавьте новый город: ')
#         if add not in a:
#             a.append(add)
#             print('Город успешно добавлен')
#         else:
#             print('Такой город уже есть')
#     elif command == 'отобразить':
#         print(', '.join(a))
#     elif command == 'удалить':
#         print(', '.join(a))
#         rem = input('Выберите город для удаления:')
#         if rem not in a:
            
#             print('Такого города нет')
#         else:
#             a.remove(rem)
#             print('Город успешно удален')
#     elif command == 'выход':
#         break

#     elif command == 'заменить':
#         print(', '.join(a))
#         replace = input('Выберите город для замены: ')
#         replace2 = input('Введите название города: ')
#         if replace  in a:
#             a.remove(replace)
#             a.append(replace2)
#         else:
#             print('Такого города нет')


# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<10:
#     if a[i]%5==0:
#         print(a[i])
#     i+=1





# for i in range(1,10):
#     for j in range (1,10):
#         print(i*j, end="\t")
#     print()