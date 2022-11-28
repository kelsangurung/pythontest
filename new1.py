print("----------LOCATION__________")
print("1.Kalanki  2.Buspark  3.Balaju")
current = int(input("Enter your current location:"))
price = 0
discount_price = 0

if current == 1:
    destination = int(input("Enter your destination"))
if destination == 2:
    student = input("Are you a student? (y/n)")
    if student == "y":
        discount_price = 15 * 0.15
        price += 15 - discount_price
    else:
        price += 15
elif destination == 3:
    student = input("Are you a student? (y/n)")
    if student == "y":
        discount_price = 30 * 0.15
        price += 30 - discount_price
    else :
        price += 30
elif current == destination:
    student = input("Are you a student? (y/n)")
    if student == "y":
        discount_price = 15 * 0.15
    price += 75 - discount_price
else :
    price += 75
if current == 2:
    destination = int(input("enter your destination:"))
if destination == 1:
    student = input("Are you a student? (y/n)")
    if student == "y":
      discount_price = 15 * 0.15
    price += 15 - discount_price
else:
    price += 15
if destination == 3:
    student = input("are you a student?(y/n)")
if student == "y":
    discount_price = 30 * 0.15
    price += 30 - discount_price
else:
    price += 30
if current == destination:
    student = input("are you a student?(y/n)")
if student == "y":
    discount_price = 75 * 0.15
    price += 75 - discount_price
else:
    price += 75

print("your price is:",price)
print("your discount ptice is :",discount_price)




