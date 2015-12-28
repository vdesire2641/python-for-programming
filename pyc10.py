# run the wallis function using 10,000 and 100,000 terms
# 2.18
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


print(wallis(10000))
print(wallis(100000))
