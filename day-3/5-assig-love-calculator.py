print("Welcome to the Love Calculator! ")
your_name = input("Please input your full name: ")
your_lover = input("Please input your lover full name: ")
matchName = your_name + your_lover

# true
t = matchName.lower().count("t")
r = matchName.lower().count("r")
u = matchName.lower().count("u")
e = matchName.lower().count("e")

# love
l = matchName.lower().count("l")
o = matchName.lower().count("o")
v = matchName.lower().count("v")
v = matchName.lower().count("e")

true = str(t + r + u + e)
love = str(l + o + v + e)

calc = int(true + love)

if calc > 99:
    calc = 99

if calc < 10 or calc > 90:
    print(f"You score is {calc} %, you go together like coke and mentos")
else:
    print(f"You score is {calc}")
