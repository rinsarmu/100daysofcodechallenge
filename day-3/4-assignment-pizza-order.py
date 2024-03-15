pizzaType = input("Please Choose type of Pizza u want? S, M or L: ")
price = 0
if pizzaType == "S":
    price = 15
elif pizzaType == "M":
    price == 20
elif pizzaType == "L":
    price = 25
addPepperoni = input("Do you want to add Pepperoni? Y or N: ")

if addPepperoni == "Y":
    if pizzaType == "S":
        price += 2
    else:
        price += 3
extra_cheese = input("Do you want to add Extra cheese? Y or N: ")

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price} ")
