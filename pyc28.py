# write a function that will return an approximate value for pi by evaluating
# the equation pi = 16(arctan1/5)-4(arctan1/239), where arctan is the arc of the tangent
# function from the math library
# PE 2.4

import math


def valpi():
    math.pi = (16(math.atan(1/5)) - 4(math.atan(1/239)))

print(" value of pi is", math.pi)
