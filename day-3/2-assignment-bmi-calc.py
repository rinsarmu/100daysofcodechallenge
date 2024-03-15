height = float(input("please input your height: "))
weight = float(input("please input your weight: "))

bmi = round(weight / (height**2), 2)

if bmi >= 35:
    print(f"Your BMI is {bmi}, you are clinically OBese ")
elif bmi >= 30:
    print(f"Your BMI is {bmi}, you are  Obese ")
elif bmi >= 25:
    print(f"Your BMI is {bmi}, you are  Overweight ")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi}, you have Normal Weight ")
else:
    print(f"Your BMI is {bmi}, you are slightly overweight")
