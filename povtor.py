# a = list(range(1, 50))
# print(a)

# a = list(range(5, 50, 3))
# print(a)

# for i in range(5,50,3):
#     if i != 35:
#         print(i)




# import time
# for hour in range(24):
#         for j in range(60):
#             for sec in range(60):
#                 print(f'{hour} часов {j} минут {sec} секунд')
#                 time.sleep(0.1)


# a=[11,1,345,254,6256,4,725,52,55545,654,62,5645,6568957,4,562,56,62,52,62,62,1,47]
# s=set(a)
# for i in s:
#     if a.count(i)>1:
#         print(i)

# t=[]
# for i in s:
#     if a.count(i)>1:
#         a=(i, a.count(i))
#         t.append(a)
# print(t)


# s=set(a)
# if len(a)!=len(s):
#     t=len(a)-len(s)
#     print('знвачения повторяюмся')
# else:
#     print('уникальны')
# print(a)
# print(s)





# nums = [1,2,3,3,3,34,56,7,8,9,0,87,5,4,3,35,5,35,54,35,634,6,4,6,3]

# nums_t = []
# for i in set(nums):
#     if nums.count(i) > 1:
#         nums_t.append((i, nums.count(i)))
# print(nums_t)


# nums_t = [(i, nums.count(i)) for i in set(nums) if nums.count(i) > 1]

# print(nums_t)


# a={
#     1:1,
#     4:4,
#     'list':{
#         'tree':3,
#         '4':43,
#         '5':5,
#         '7':7}
# }

# print(a['list']['4'])
# s={}
# for i,j in a['list'].items():
#     s[i]=j
#     break
# print(s)

# s={}
# for key,value in a['list'].items():
#     if key=='tree':
#         s[key]=value
# print(s)

import subprocess
systemInfo = ''
try:
    systemInfo = subprocess.check_output(['uname']).decode('utf-8', errors="backslashreplace").split('\n')
    systemInfo = systemInfo[0]
except :
    pass
if systemInfo == "Linux":
    wifiData = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections']).decode('utf-8', errors="backslashreplace").split('\n')
    print ("Wifi                            Password")
    print ("----------------------------------------")
    for wifiname in wifiData:
        if wifiname != '':
            wifiPass = subprocess.check_output(['sudo','cat', f"/etc/NetworkManager/system-connections/{wifiname}"]).decode('utf-8', errors="backslashreplace").split('\n')
            password=wifiPass[15].strip("psk=");
            print ("{:<30} {:<}".format(wifiname, password))
else:
    wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except :
                print ("{:<30}|  {:<}".format(i, ""))
        except :
            print ("{:<30}|  {:<}".format(i, "ОШИБКА КОДИРОВАНИЯ"))




