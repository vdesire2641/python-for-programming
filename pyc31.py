# write a function that will return an approximate value of pi by evaluating
# the equation pi=sqrt12(1-1/3*3 + 1/5*3^2 - 1/7*3^3 + ...)
# use a parameter called n to denote the number of terms to include in the summation.
# PE 2.7

import math


def valpi(n):

    math.pi = math.sqrt(12) * (1-(1 / 3 * 3) + (1 / 5 * 3 ^ 2) - (1 / 7 * 3 ^ 3))
print("value of pi is", math.pi)

valpi(3)




