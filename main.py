# data = [
#     ['ram', 'sita', 'gita'],
#     ['hari', 'shyam', [[["laxmi"]]], 'gopal'],
#
# ]
# print(data[1][3])

# name = 'ram'

# data = ['ram', 'sita', 'gita']
# print(data)
# data[0] = 'kel'
# print(data)

# data = ['ram', 'sita', 'gita']

# data = {
#     'name': 'kel',
#     'age': 20,
#     'address': [
#         {'location': 'kathmandu'},
#         {'street': 'baluwatar'}
#     ]
# }
# print(data['address'][1]['street'])


# username = input("enter username")
# password = input("enter pasw")
# if username == "ram" and password == "1234" or username == "ram002" and password == "1234":
#      print ("welcome")
# else:
#     print ("INVALID USER")

# x = 12
# y = 10
# z = 15
#
# if x > y :
#     if x > z:
#         print("x is greater")
#     else:
#         print("z is greater")
# else:
#     if y > z:
#         print("y is greater")
#     else:
#         print("z is greater")


# username = input("enter username")
# password = input("enter password")
# if username == "ram":
#     if password == "1234":
#         print("login complete")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")

#
# x = 2
# if x %2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

#
# principle = int(input("enter principle:"))
# time = int(input("enter time:"))
# rate = int(input("enter rate:"))
# simple_interest = principle * rate * time / 100
# print("simple interest is:",simple_interest)


#
# x=6
# y=9
# z=5
# if x > y and x > z


# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# if num1 >= num2 and num1>= num3:
#     largest = num1
# elif num2 >= num1 and num2>=num3:
#     largest = num2
# else:
#     largest = num3
# print("the largest number is:",largest)


# for a in range(1,6):
#     print('hello sophia')

# for a in range(1,6):
#     print('hello sophia')
#     break

# data = [1, 2, 3, 4, 5, 6, 7, 8]
# for x in data:
#     print(x)

# x=1
# while x < 10:
#     print(x)
#     x += 2

# x=1
# names = []
# while x <= 3:
#     name = input('enter your name:')
#     names.append(name)
#     x += 1
# for name in names:
#     print(f"Hello {name}")

# x = 1
# names = []
# while x <= 3:
#     name = input('enter name:')
#     names.append(name)
#     x += 1
# for name in names:
#     print(f"hello {name}")


# data  = [
#     [12, 13, 14, 15],
#     [16, 17, 18, 19],
#     [20, 21, 22, 23],
# ]
# for a in data:
#     for b in a:
#         print(b)
#     print("---------------")

# num_of_times = int(input('enter number of times:'))
# increment = 1
# data = []
#
# while increment <= num_of_times:
#     num =  int(input('enter number:'))
#     data.append(num)
#     increment += 1
#
# rep_num = []
# for x in data:
#     if data.count(x) > 1 and x not in rep_num:
#         rep_num.append(x)
#
# for y in rep_num:
#     print(f"{y} is repeated {data.count(y)} times")


# data = [12, 3, 4, 4, 4]
# print(data.count(4))
# print(data)
# data.append(60)
# data.append(70)
# print(data)

# data=[]
# print(dir(data))

# x = int(input("enter x:"))
# y = int(input("enter y:"))
# z = int(input("enter z:"))
# if x > y and x > z:
#     if y > z:
#         x, y, z = x, y, z
#     else:
#         x, y, z =  x, z, y
# elif y > x and y > z:
#     if x > z:
#         x, y, z = y, x, z
#     else:
#         x, y, z = y, z, x
# elif z > x and z > y:
#     if x > y:
#         x, y, z = z, x, y
#     else:
#         x, y, z = z, y, x
# else:
#     x, y, z = x, y, z
# print(f"Sorted numbers: {x} , {y}, {z}")



# data = ['ram, sita, hari, ram, haru']
# ram enter handa kati ota ram cha bhanera nikalne
# #ram
# #ram,ram
# yesto aunu paro
#
# num_of_times = int(input('enter number of times:'))
# increment = 1
# data =[]
#
# while increment <= num_of_times:
#     name = input("enter your name:")
#     data.append(name)
#     increment += 1
# rep_name = []
# for x in data:
#     if data.count(x) > 1 and x not in rep_name:
#         rep_name.append(x)
# for y in rep_name:
#         print(f"{y} is repeated {data.count(y)} times")


# name = input("enter name:")
# age = input("enter age:")
# phone = input("enter phone num:")
# address = input("enter address:")
# print(f"My name is {name} and i am {age} years old.I'm from {address} and my phone number is {phone}")

#
# list1 = ["kelsang",19,98455,55.5]
# print(list1)

# list1.append('Kel')
# print(list1)
#
# list1.insert(6, 'kels')
# print(list1)
#
# list1.pop()
# print(list1)
#
# list1.remove(19)
# print(list1)

# list1[0]= 'kelsu'
# print(list1)

# print(list1.count('kelsang'))
# print(list1)


# HOMEWORK
# DATA TYPES
# variable,rule
# types conversion
# numbers, strungs,list,tuple,sets,dictionary
# condtion statement : ef elif else nested if else
# loops :for while, nested loop
# funtions:introduction
# modules:introduction

# data ={
#     'name': "sophia",
#     'age':12,
#     'phone':912123123,
#     'address': "kathmandu",
#     "town":{
#         "name": "putalisadak",
#         "tole": {
#             "name":"kamaldi",
#         }
#     }
#
# }
# print(data["town"]["tole"]["name"])

# data ={
#     'name': "sophia",
#     'age':12,
#     'phone':912123123,
#     'address': "kathmandu",
#     "town":{
#         "name": "putalisadak",
#         "tole": {
#             "name":"kamaldi",
#             "ward": [
#                 1,2,3,4,5,6,7,8,9,10
#             ]
#         }
#     }
#
# }
# print(data["town"]["tole"]["ward"][4])

# data ={
#     'name': "sophia",
#     'age':12,
#     'phone':912123123,
#     'address': "kathmandu",
#     "town":{
#         "name": "putalisadak",
#         "tole": {
#             "name":"kamaldi",
#         },
#     },
#     "students":[
#         {
#             "name":"amul",
#         }
#     ]
#
# }
# print(data["students"][0]['name'])


# data ={
#     'name': "sophia",
#     'age':12,
#     'phone':912123123,
#     'address': "kathmandu",
#     "town":{
#         "name": "putalisadak",
#         "tole": {
#             "name":"kamaldi",
#         },
#     },
#     "students":[
#         {
#             "name":"amul",
#         }
#     ]
#
# }
# print(data["students"][0]["name"])

