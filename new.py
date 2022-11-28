print("--------Computer Bazar--------")
print("1. Dell(Rs:1000) 2.Toshiba(2000) 3.Mac(30002")
option = int(input("enter your option:"))
dell_price = 0
toshiba_price = 0
mac_price = 0
price = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
giftbox_price = 0
location_price = 0
tax_amount = 0

if option == 1:
    quantity = int(input("enter the quantity:"))
    dell_price = quantity * 1000
elif option == 2:
    quantity = int(input("enter the quantity:"))
    toshiba_price = quantity * 2000
elif option == 3:
    quantity = int(input("enter the quantity:"))
    mac_price = quantity * 3000
else:
    print("INVALID OPTION")
    exit()

print("1.Home(Rs.1000) 2.Pickup(free)")
delivery_option = int(input("enter your location:"))
if delivery_option ==1:
    delivery_price = 1000
print("1.Plastic(RS.500) 2.Bag(RS.1000) 3.Giftbox(Rs.5000)")
packing_option = int(input("enter packing option:"))
if packing_option == 1:
    plastic_price = 500
elif packing_option == 2:
    bag_price = 1000
elif packing_option == 3:
    giftbox_price = 5000

total = dell_price + toshiba_price + mac_price
print("1.Kathmandu(Rs.13% tax) 2.Bhaktapur(FREE) 3.Lalitpur(FREE)")
location_option =int(input("Enter location option"))
if location_option == 1:
    tax_amount = total * 0.13

grand_total = total + delivery_price + plastic_price +bag_price + giftbox_price + tax_amount
print("-----BiLL-----")#
print("total:",total)
print("tax:",tax_amount)
print("Grand Total:",grand_total)








