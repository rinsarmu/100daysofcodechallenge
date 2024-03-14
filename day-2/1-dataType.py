#Int
# int is for every integers eg age=20

#Float
#float is for floating numbers. when decimal number floats between numbers. 
#eg pi=3.14

#String
#string is for any text

    #Substrign : if we want to access the single characters of the string that is substring we can do it like this. print("hello"[1]). this prints e from hello.

#Boolean
#for the value true or false.

# to know the type of dataype we can use type() method.
# eg type(3.14) // <class 'float'>
print(type(3.14))

#in python we cant implicitly concatenate numbers with string. because they have differet data type. to make that happen we may use str() method.

print('Pi in mathematics is '+ str(3.14)) #Pi in mathematics is 3.14

#unless I use str() method it flags error message.

#TYPE CONVERSION METHODS
#str()
#float()
#int()

print(int(3.14)) # 3
print(str(3.14)) # 3.14
print(float(3)) # 3.0
