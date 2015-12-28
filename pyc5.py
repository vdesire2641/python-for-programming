# function tht returns the average of the first n numbers
# where n is the parameter
# 2.11
def average(n):
    a = 0
    for i in range(1,n+1,1):
        a = a + i
    b = a/n
    print(b)
    return(b)

average(10)



