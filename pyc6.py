# function called factorial that computes the
# product of first n numbers
# where n is a parameter
# 2.12
def factorial(n):
# the very first number should be 1 not 0
    a = 1
    for i in range(2,n+1,1):
# factorial is the product of all the numbers
# in the given range
        a = a * i
    return(a)

print (factorial(6))
