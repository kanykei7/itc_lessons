# try:
#     a=int(input('chislo a\n>> '))
#     b=int(input('chislo b\n>> '))
    # print(a/b)
# except ZeroDivisionError:
#     print('на 0 делить нельзя')
# except NameError:
#     print('нет такой переменной!')
# except ValueError:
#     print('введите только цифры')




# while True:
#     try:
#         a=int(input('chislo a\n>> '))
#         b=int(input('chislo b\n>> '))
#         print(a/b)
#     except ZeroDivisionError:
#         print('на 0 делить нельзя')
#     except NameError:
#         print('нет такой переменной!')
#     except ValueError:
#         print('введите только цифры')



# try:
#     a=int(input('chislo a\n>> '))
#     b=int(input('chislo b\n>> '))
#     print(a/b)
# except:
#     print('поймал все ошибки')
# else:
#     print('не поймал ни одну ошибку')
# finally:
#     print('finally')


# try:
#     print('d'/5)
# except TypeError as e:
#     print(f'код вырубился из-за ошибки: {e}')

# a=[2,3,4,5,6,7,8,9,9,10]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(True)
#     else:
#         b.append(False)
# print(all(b))
# print(any(b))
# print(b)


# a=[2,3,4,5,6,7,8,9,9,10]
# print(min(a))
# print(max(a))
# print(sum(a))

# b=reversed(a)
# print(list(b))


# print(eval('9+5'))

# while True:
#     eval(input('>>>'))

# print(slice(a,5,2))

# a=10/3
# print(round(a))#округляет


# dict_={
#     'name':'john',
#     'lastname':'snow',
#     12:'age'
# }
# try:
#     for x in dict_.keys():
#         x+'abc'
#         print(x)
# except TypeError:
#     if type(x)==int:
#         a=str(x)
#         print(x)
# from statistics import mean


# c=[]
# while True:
#     try:
#         b=input('chislo:\n>>')
#         a=int(b)
#         if type(a)==int:
#             c.append(int(b))
#     except:
#         break
# print('You entered:',c)
# d=0
# for i in c:
#     d+=i
#     rez=d/len(c)
# print('Total:' ,d)
# print('Average:', rez)

# print('Average:', mean(c))

# Задание 4
# Необходимо написать программу, которая считывает числа, вводимые пользователем, пока пользователь не введёт слово “end”. Предполагайте, 
# что пользователь вводит только целые числа или слово “end”. В конце программа должна вывести все введенные числа через запятую и их сумму и среднее значение.


# Пример вывода:


# Enter numbers:

# 1

# 10

# 25

# -1

# 0

# 3

# 67

# end

# You entered: 1, 10, 25, -1, 0, 3, 67

# Total: 105

# Average: 15.0


# Указания:

# Используйте цикл while для ввода чисел и сохраняйте их в списке.
# Используйте цикл for для подсчета суммы чисел в полученном списке.


s = []
n = input('Введи число или end для завершения: ')

while n != 'end':
    if not n.isdigit():
        print('Вы ввели не цифру введите корректно')
        n = input('Введи число или end для завершения: ')
        continue
    s.append(int(n))
    n = input('Введи число или end для завершения: ')
else:
    # ful = []
    # for i in s:
    #     ful.append(str(i))
    # ful = ', '.join(ful) 

    # print('your digits: ', ful)

    print('your digits: ', ', '.join(str(i) for i in s))
    print('summ: ', sum(s))
    print('Arif: ', sum(s)/ len(s))