# write a function that will return an approximate value of pi by evaluating the
# equation pi=ln(640230^3 + 744)/sqrt163 , where ln is the log function from
# math library
# PE 2.5

import math

def valuePi():
    math.pi = (math.log10(640320^3 + 744))/math.sqrt(163)

print("the value of pi is", math.pi)