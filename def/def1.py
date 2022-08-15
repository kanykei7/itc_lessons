# a=[1,2,3,4,5,6,7,8,5,8,44,9]
# b=[1,2,3,4,5,6,7,8,5,8,44,9,7,99]


# def my_len():
#     s=0
#     for i in a:
#         s+=1
#     print(s)
# my_len()

# def my_len(massiv):
#     s=0
#     for i in massiv:
#         s+=1
#     return s
# print(my_len(a))
# print(my_len(b))



# def my_sum(a,b):
#     return a+b
# print(my_sum(4,7))




# list_1=['name','age','1','19']
# pop=['kani','manu','age','friend','azamat','eliza','iphone']

# def func(l):
#     a=l[:len(l)//2]
#     b=l[len(l)//2:]
#     a.reverse()
#     b.reverse()
#     a.extend(b)
#     return a
# print(func(list_1))
# print(func(pop))


# n=10
# def func(n):
#     a=1
#     b=1
#     i=0
#     while i<n-2:
#         c=a+b
#         a=b
#         b=c
#         i+=1
#         print(a)
#     return b
# print(func(n))



# def sloj(a,b):
#     return a+b

# def vych(a,b):
#     return a-b

# def vyzov(a,b):
#     return(sloj(a,b),vych(a,b))
# print(vyzov(5,5))


# import os
# n=input('имя файла:\n>> ')
# def f(n):
#     return os.system(f'touch {n}')
# a=f(n)
# print(a)

from random import choice
a='145790' 

def gen_number(a):
    new_a=''
    while len(new_a)<6:
        new_a+=choice(a)
    return(f'0444{new_a}')
print(gen_number(a))


























# n=int(input('>>>'))
# def fibon(n):
#     fib1=1
#     fib2=1
#     i=0
#     while i<n-2:
#         sum=fib1+fib2
#         fib1=fib2
#         fib2=sum
#         i=i+1
#         return fib2
# print(fibon(10))

# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)
