import math

def archimedes (numsides):

	innerangleB = 360.0/numsides
	halfangleA = innerangleB/2

	onehalfsideS = math.sin(math.radians(halfangleA))

	sideS = onehalfsideS * 2

	polygonCircumference = numsides * sideS
	pi = polygonCircumference/2

	return pi

archimedes(8)
for sides in range(8, 100, 8):
    print(sides, archimedes(sides))