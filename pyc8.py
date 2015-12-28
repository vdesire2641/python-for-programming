# compute the fibonacci series
# taking output from the user
# 2.13
# 2.14
def fibonacci(n):
# we have been given the first two numbers
# of the sequence
    a, b = 1, 1
    for i in range(1, n, 1):
# fibonacci sequence is the sum of previous two numbers
        if n>= 3:
            a, b = b, a + b
        else:
            print('number less than 3')
    return(a)
    return(b)

print(fibonacci(4))
