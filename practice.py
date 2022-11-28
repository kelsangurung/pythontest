# username = input('enter username:')
# password = input('enter password:')
# if username == 'kel' and password == '1234':
#     print('WELCOME USER')
# elif username == 'kel' and password != '1234':
#     print('INVALID PASSWORD')
# else:
#     print('INVALID USER')

# data = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# for a in data:
#     for b in a:
#       print(b)

# num_of_times = int(input("enter number of times:"))
# increment = 1
# data = []
# while increment <= num_of_times:
#     num = int(input("enter a number:"))
#     data.append(num)
#     increment += 1
# rep_num = []
# for x in data:
#     if data.count(x) > 1 and x not in rep_num:
#         rep_num.append(x)
# for y in rep_num:
#     print(f"{y} is repeated {data.count(y)} times")


# x = int(input("enter x:"))
# y = int(input("enter y:"))
# z = int(input("enter z:"))
# if x > y and x > z:
#     if y > z:
#         x, y, z = x, y, z
#     else:
#         x, y, z = x, z, y
# elif y > x and y > z:
#     if x > z:
#         y, x, z = y, x, z
#     else:
#         y, x, z = y, z, x
# elif z > x and z > y:
#     if x > z:
#         z, x, y = z, x, y
#     else:
#         z, x, y = z, y, x
# else:
#     x, y, z = x, y, z
# print(f"Soretd numbers:{x}, {y}, {z} ")

# x = 1
# names = []
# while x <= 3:
#     name = input('enter name:')
#     names.append(name)
#     x += 1
# for name in names:
#     print(f"Hello {name}")



# def welcome(name,age,address=''):
#     print(f"welcome to python,{name} who is {age} years old and lives in {address}")
# welcome('kelsang',19,'baluwatar')

