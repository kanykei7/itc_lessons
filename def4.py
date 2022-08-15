#=================ЛЯМБДА=====================

# sum_arg=lambda a: a**2
# print(sum_arg(9))


# s=(lambda a,b: a+b)(5,7)
# print(s)


# a=[2,3,4,5,6,7,8,9]
# for i in range(len(a)):
#     a[i]=(lambda x:x**2)(a[i])
# print(a)


# print(list(map((lambda x:x**2),a)))


# s=(lambda x, n:n*100/x)(150,75)
# print(s)



# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)


# def hell(x):
#     if x!=0:
#         print(x)
#         x-=1
#         hell(x)
#     else:
#         print('finish')

# hell(50)

# x=10+1
# while x!=0:
#     x-=1
#     print(x)
# print('finish')


# def derive(coefficient, exponent): 
#     rez=coefficient*exponent
#     return f'{rez}x^{exponent-1}'
# print(derive(7, 8))

# def even_or_odd(number):
#     if number%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
# print(even_or_odd(7))


# def repeat_str(repeat, string):
#     return string*repeat
# print(repeat_str('Hello',7))

# from string import ascii_letters
# def get_char(c):
#     return len() 
# print(get_char('A'))

# def count_by(x,n):
#     a=[]
#     for i in range(x,n+1,x):
#         a.append(i)
#     return a
# print(count_by(2,5))

# def count_by(x,n):
#     a=[]
#     b=[]
#     for i in range(1,n):
#         a.append(i)
#     for j in a:
#         l=a[x:len(a):x]
#         b.append(j)
#     print(l)
#     # print(b)
#     # return a
# print(count_by(2,10))


# def square_sum(*numbers):
#     a=[]
#     for i in numbers:
#         rez=i**2
#         a.append(rez)
#     b=0
#     for j in a:
#         b+=j
#     return b
# print(square_sum(2,2,2))

# def square_sum(numbers):
#     rez = 0
#     for num in numbers:
#         rez = rez + num*num
#     return rez


# @test.describe("Basic tests")
# def _():
#     test.assert_approx_equals(guess_blue(5, 5, 2, 3), 0.6)
#     test.assert_approx_equals(guess_blue(5, 7, 4, 3), 0.2)
#     test.assert_approx_equals(guess_blue(12, 18, 4, 6), 0.4)


# blue=12
# red=18
# tblue=4
# tred=6
# rez=blue-tblue
# rez1=red-tred
# rez2=rez+rez1
# rezblue=rez*100/rez2
# print(rezblue/100)


# def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
#     pull_blue=blue_start-blue_pulled
#     pull_red=red_start-red_pulled
#     sum_pulled=pull_blue+pull_red
#     rez_blue=pull_blue*100/sum_pulled
#     return rez_blue/100
# print(guess_blue(12, 18, 4, 6))



# def fake_bin(x):
#     a=[]
#     for i in x:
#         b=int(i)
#         if b>=5:
#             a.append(1)
#         else:
#             a.append(0)
#     return a
# print(fake_bin('12345678976523'))


# def fake_bin(x):
#     a=''
#     for i in x:
#         if int(i)>=5:
#             a+='1'
#         else:
#             a+='0'
#     return a
# print(fake_bin('12345678976523'))



# def find_smallest_int(*arr):
#     return min(arr)
# print(find_smallest_int(1,2,3,4,5,-1))


# def find_smallest_int(*arr):
#     a=0
#     for i in arr:

#         if i<i:
#             return i
# print(find_smallest_int(1,2,3,4,55,9))


# def func(n):
#     a=''
#     while len(str(n)):
#         for i in n:
#             a-=i
#     return a
# print(func(1234567))


# def func(n):
#     a=''
#     for i in range(1,n+1):
#         a+=str(i)+'sheep...'
#     return a
# print(func(1))
# print(func(2))
# print(func(3))



# func=lambda n:list(f'{(i+1)} sheep...' for i in range(n))
# print(func(1))
# print(func(2))
# print(func(3))
# func=lambda n:''.join(f'{i+1} sheep...' for i in range(n))


'''
.
⠄⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄
⣿⣿⣿⣿⣿⣿⡟⠃⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⣿⣿⣿⣿⣿⠋⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡏⠈⠉⡯⣄⣀⣉⣉⡉⠉⠄⠄⢸⡷⣿⣿⣿⣿⣿⣿⡿⠁
⣿⣧⠠⠄⠁⠹⣿⣿⣛⠿⠂⠄⠄⠸⣷⣿⣿⣿⣿⣿⣿⠁
⣿⣿⡲⡄⠄⠄⠄⠈⠄⠄⠄⠄⠄⠄⠘⡟⣿⣿⣿⣿⣿
⣿⣿⢹⡇⠄⠄⠄⠄⠄⠄⢀⣀⡀⠄⠈⠄⢿⣿⣿⣿⠁
⣿⣿⠄⠈⠠⡀⠄⠄⠄⠠⣀⠈⠁⠄⢀⣤⣿⣿⠏⠹⡇
⣿⣿⠄⠄⠄⠈⠳⣆⡀⠄⠄⢀⣤⣾⣿⣿⣿⣿⣷⣦⣁
⠉⠹⢶⣤⡀⠄⠄⠈⠙⢿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⠷⣦⣤⣀⡀
⠄⠄⠈⢿⣿⣦⡀⢀⣀⠄⠙⠻⣿⣿⣷⣦⠈⠛⣿⣿⣿⣷⣦⣌⠛⠻⢶⣤⡀
⠄⠄⠄⠄⣿⣿⠄⠉⠁⠄⠄⠤⢍⢫⡿⢿⣷⡀⠈⠻⠿⣿⣿⣿⣿⣶⣀⠙⢿⣆
⠄⠄⠄⢰⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣽⢻⠄⠄⠄⠄⠄⠈⠙⢿⣿⣷⣌⢹
⠄⠄⠄⠄⠻⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⢒⣶⡂⠄⠄⠄⠄⠄⠄⠹⣿⣿⣶
⠄⠄⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢹⡲⣀⡔⠄⠄⠄⠄⠄⢻⣿⣿
⠄⠄⠄⠄⠄⠄⢠⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢈⣉⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿
⠰⡄⠄⠄⣠⣤⣤⣧⡄⠄⠄⠄⠄⠄⠄⠄⠄⡴⣼⣿⣦⣄⠄⠄⠄⠄⠄⣾⣿⣿
⠄⢰⣶⣿⣿⣿⣿⣿⣇⡀⢀⣴⣶⣦⣄⡒⣽⢳⡟⠛⢿⡋⠁⠄⠄⣀⣼⣿⣿⣿
⠄⠄⠹⠿⠛⢉⣙⢿⣿⣕⣾⢹⣿⡿⢋⡞⠏⠄⠄⢀⣈⠛⠻⣿⣿⣿⣿⣿⣿⣿
⣸⣿⢠⡄⠿⠘⠚⠄⢞⢉⡧⠄⠄⠄⠈⣠⠴⠒⠋⡹⠋⠄⠄⢿⣿⣿⣿⣿⣿⣿
⠙⣿⣿⡉⡐⠴⠘⣓⠸⣄⣾⣦⠄⡾⠛⠁⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿
⠄⠈⠁⠋⠃⣠⡄⠻⢃⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿⣿⡿⠋
⠄⠄⠄⠄⠛⠠⣴⣾⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄⡀⠄⢀⣿⣿⣿⣿⣇
⠄⠄⠄⠄⣀⣀⢿⣿⣿⣿⣿⣿⣟⣷⠄⠄⠄⠄⠄⠄⡇⠄⢸⣿⣿⣿⣿⣿⡄
⣀⡔⠊⡹⣿⡀⠈⢿⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠆⠄⢸⣿⣿⣿⣿⣿⣇
⣿⣧⠄⠘⣿⢷⡶⠾⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⡞⢿⣿⣿⣿⣿⣿
⣿⣿⢳⠄⠘⢺⣿⣶⡝⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⢀⠃⠸⣿⣿⣿⣿⣿⡆
'''
