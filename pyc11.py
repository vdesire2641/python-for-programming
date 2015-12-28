# archimedes function
import math

def archimedes (numsides):

	innerangleB = 360.0/numsides
	halfangleA = innerangleB/2

	onehalfsideS = math.sin(math.radians(halfangleA))

	sideS = onehalfsideS * 2

	polygonCircumference = numsides * sideS
	pi = polygonCircumference/2

	return pi

# leibniz function
def leibniz(terms):
    acc = 0
    num = 4
    den = 1

    for aterm in range(terms):
        nextterm  = num/den * (-1)**aterm

        acc = acc + nextterm

        den += 2

        return acc


# wallis function
def wallis(pairs):
    acc = 1
    num = 2

    for apair in range(pairs):
        leftterm = num/(num-1)
        rightterm = num/(num+1)

        acc = acc * leftterm * rightterm

        num = num + 2

    pi = acc * 2
    return pi


