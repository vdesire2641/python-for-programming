# write a function to complete the volume of sphere with a radius of r.
# use r as the parameter to the function. use pi from the math module
# PE 2.3

import math

def vol(r):
    volumeOfsphere = 4/3 * math.pi * r * r * r

    print("volume of sphere is", volumeOfsphere)

vol(6)