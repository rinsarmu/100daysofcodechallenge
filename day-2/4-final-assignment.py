print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
numOfPeople = int(input("How many people to split the bill? "))

tip = bill * (percentage / 100)

totalBill = bill + tip
billPerPerson = totalBill / numOfPeople
roundedResult = round(billPerPerson, 2)
print(f"Each Person should pay: ${roundedResult}")
