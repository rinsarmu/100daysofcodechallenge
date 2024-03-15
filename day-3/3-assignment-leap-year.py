# leap year is a year divided by 4 and not by 100. if it is divided by 100 and by 400 it is also leap year. if it is divided by 4 , 100 and not 400 it is not leap year.

currentYear = int(input("Please enter current Year: "))

if currentYear % 4 == 0:
    if currentYear % 100 == 0:
        if currentYear % 400 == 0:
            print(f"----{currentYear} is a Leap Year ----")
        else:
            print(f"----{currentYear} is not Leap Year----")
    else:
        print(f"----{currentYear} is a Leap Year----")
else:
    print(f"---- {currentYear} is not Leap Year ----")
