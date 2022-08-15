# hel=input('>>')
# def new_func(hel):
#     a='1234567890_qwertyuiopasdfghjklzxcvbnm'
#     if len(hel)>=4 and len(hel)<=16:
#         for i in hel:
#             if i not in a:
#                 return False
#         else:
#             return True
#     else:
#         return False
# print(new_func(hel))



# import re
# def validate_usr(username):
#     return bool(re.fullmatch('[a-z_0-9]{4,16}',username))



# def count_positives_sum_negatives(arr):
#     if len(arr) == 0:
#         return []
#     a=0
#     b=0
#     for i in arr:
#         if i>0:
#             a+=1
#         if i<0:
#             b+=i
#     return [a ,b]

# print(count_positives_sum_negatives([1,2,3,4,-4,-8,0,2]))


# def am_i_wilson(n):
#     d=2
#     while n%d!=0:
#         d+=1
#     return d==n

# print(am_i_wilson(6))



# def func(n):
#     k = 0
#     for i in range(2, n // 2+1):
#         if (n % i == 0):
#             k = k+1
#     if (k <= 0):
#         return True
#     else:
#        return False
# print(func(1))




# def am_i_wilson(n):
#     if n==0 or n==1:
#         return False
#     if n ==2:
#         return True 
#     k = 0
#     for i in range(2, n // 2+1):
#         if (n % i == 0):
#             k = k+1
#     if (k <= 0):
#         return True
#     return False


# def collatz(n):
#     a=[n]
#     while n>1:
#         if n%2==0:
#             n=n//2
#         else:
#             n=n*3+1
#         a.append(n)
#     return  a[0], len(a)
# print(collatz(20))


# hanoi = lambda disks: 2**disks-1


# 15
# 46
# 23
# 70
# 35
# 106
# 53
# 160
# 80
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# def zeros(n):
#     fact = 1
#     a=''
#     for i in range (1, n+1):
#         fact = fact * i
#     return fact
# print(zeros(30))


# def zeros(n):
#     fact = 1
#     a=''
#     for i in range (1, n+1):
#         fact = fact * i
#     a+=str(fact)
#     c=a[::-1]
#     d=[]
#     for i in c:
#         if i=='0':
#             d.append(0)
#         else:
#             break   
#     return d
# print(zeros(30))



# def zeros(n):
#     fact = 1
#     a=''
#     for i in range (1, n+1):
#         fact = fact * i
#     a+=str(fact)
#     c=a[::-1]
#     count = 0
#     for i in c:
#         if i=='0':
#             count += 1
#         else:
#             break   
#     return count

