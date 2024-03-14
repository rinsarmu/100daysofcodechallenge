age = int(input("What is your current age? "))
maxyear = int(input("Can you predict maximum number of year u will live? "))
maxYear = 90
leftYear = maxYear - age

months = leftYear * 12
weeks = leftYear * 52
days = leftYear * 365

print(f"You have {days}, {weeks} weeks, and {months} months left")
