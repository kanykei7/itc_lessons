'''
a=5
b=3
print(a//b)

a=2
b=2
print(a**b)

a=5
b=3
print(a//b)

a=25
b=5
print(a%b)

a=(17*3)
b=(12*5)
print(a>b)

a=12**3
b=13*7
print(a>b)

a =4**5
b =512+512
print(a==b)

m=17925
a=34**2
b=26*3
c=17*33
d=4394*4
print(m>=a)
print(m>=b)
print(m>=c)
print(m>=d)


a=4
b=5
c=9
d=2
e=193432
print(a+b*c**d-e)

a=5
b=2
c=6
print(a>b and a<c)

a=7
b=3
c=4.8
print(a%b*c)

a=10+2
b=6+6
print(a==b)

a=57+77
b=6*78
print(a!=b)'

print(-21//10)

a=2003
b=2021
print(b-a+2)
print(b-a-2)

a=18
b=100
print((a/b)*100)

a=25
b=75
c=10
d=95
print(a+b+c+d/4)

a=2.2
b=2.2
c=2.2
print(a+b*c)

a=6
b=7
c=20
d=3
e=12
print((a-e**(b/d))%c)



a=[63675, 888, 17925]
b=17925
for i in a:
	if i==b:
		print(i)
	else:
		print('no')


main = 17924
a=int(input('chislo'))
move = int(input('1**\n2*\n'))
b=int(input('chislo'))

if move==1:
	rez=a**b
	print(rez)
	if rez<main:
		print('menshe')

		if rez==main:
			print('ravno')

	else:
		print('bolshe')
if move==2:
	rez=a*b
	print(rez)
	if rez<main:
                print('menshe')

        	if rez==main:
                	print('ravno')

	else:
		print('bolshe')
else:
	print('no')
'''
