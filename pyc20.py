# write a function that takes three integers as parameters and returns the largest
# 2.34
def integers(a, b, c):
    if (a>b and a>c):
        print("largest integer", a)
    else:
        if (b>a and b>c):
            print("largest integer", b)
        else:
            if (c>a and c>b):
                print("largest integer", c)


integers(5000, 10, 800)