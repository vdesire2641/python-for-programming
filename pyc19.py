# a year is a leap year if it is divisible by 4 unless it is a century no divisible
# by 400. write a function that takes a year as a parameter and returns true
# if the year is a leap year and false otherwise
# 2.32
def leapyear(year):
    if (year % 100 == 0):
        print(" this is century")
        if (year % 4 ==0 and year % 400 == 0):
            print("true")
        else:
            print("false")
    else:
        print(" this is not a century")
        if (year % 4 == 0):
            print("true")
        else:
            print("false")

leapyear(3000)
