import random

# in this case am going to accept names of the people and randomly choose the person who gonna pay the cash.
names_list = input("Give me name of the peoples: ")

# using split method i explicity changed string into list.
names = names_list.split(",")

# using len method i get the length of the list.
totalPeople = len(names) - 1

# using random i get certain random number
randomPerson = random.randint(0, totalPeople)

print(f"{names[randomPerson]} is going to be punished.")
