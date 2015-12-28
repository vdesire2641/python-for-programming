# run the leibniz function using 10,000 and 100,000 terms
# 2.15
def leibniz(terms):
    acc = 0
    num = 4
    den = 1

    for aterm in range(terms):
        nextterm = num/den * (-1)**aterm

        acc = acc + nextterm

        den = den + 2

    return acc

print(leibniz(10000))
print(leibniz(1000000))


