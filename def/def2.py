# def square(a,b=2):
#     return a**b
# print(square(9,3))

# def login(name, age=18):
#     return f'your name = {name}, your age = {age}'
# print(login('kani'))

# def func(*args):
#     for i in args:
#         if i % 2 == 0:
#             return(i)
# print(func(1,2,3,4,5,6,7,8,9))


# def func(**kwargs):#возвращает словарь
#     return kwargs
# print(func(name='aktan', age=17))

# def chet(x):
#     if x % 2 == 0:
#         return f'{x} четное'
#     else:
#         return f'{x} нечетное'
# for i in range(1,11):
#     print(chet(i))

# def chetnoe(x):
#     if x % 2 == 0:
#         return True
#     return False
# # print(chetnoe(7))



# for i in range(1, 20):
#     if chetnoe(i):
#         print(i, 'четное')


# def add(a,b):
#     return a+b
# def substract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# print(add(66,6))
# print(substract(66,6))
# print(multiply(66,6))
# print(divide(66,6))


# a='привет меня зовут каныкей пока'
# def func(a):
#     count=0
#     for i in a:
#         count+=1
#     return count
# print(func(a))

# a={
#     'name':'kanykey',
#     'age':18
# }
# b={
#     'name':'eliza',
#     'age':16
# }
# def vm(a,b):
#     a.update(b)
#     return a
# print(vm(a,b))

# def func():
#     a=input('чтобы вы хотели покушать?\n>> ')
#     b=input('чтобы вы хотели попить?\n>> ')
#     with open('file.txt', 'a+') as f:
#         f.write(a)
#         f.write(b)
#         return f
# print(func())

# import os
# n=input('имя файла:\n>> ')
# def f(n):
#     return os.system(f'touch {n}')
# a=f(n)
# print(a)

# def func():
#     print('first')
#     def func1():
#         print('second')
#     func1()
# func()


# a={
#     'name':'kanykey',
#     'age':18
# }
# def func(a,*args,**kwargs):
#     b=[]
#     # b.append(a.keys())
#     # print(b,args)
#     if args:
#         b.append(args)
#         print(args)
#     # print(a.keys(),a.values())
# func(a)


# a=[]# находим простые числа 
# for i in range(2,100):
#     k=0
#     for j in range(2,i):
#         if i % j == 0:
#             k+=1
#     if k == 0:
#         a.append(i)
# print(a)


# def func(*args):
#     return args
# print(func(1,2))

# def func(a,b):
#     return [a,b]
# print(func(1,2))

# a=int(input('>> '))
# def func(a):
#     for i in range(a+1):
#         print(f'wtf {i}')
# print(func(a))

# def func(a,b=5000):
#     return f'{a}-{b}'
# print(func('kani'))

# def func(n):
#     l=[]
#     for i in range(n):
#         l.append(i+1)
#     print(*l) 
# print(func(10))







