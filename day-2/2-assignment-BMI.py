name = input('Enter Name of the Person: ')
height = float(input('please '+ name+ ' height: ')) 
weight = float(input('please '+ name+ ' weight: '))

bmi = int( weight / height ** 2)

print("BMI of "+ name + " is: "+ str(bmi))
