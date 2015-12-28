# write a function that takes two parameters- a pay rate and
# the number of hours worked- and returns the pay. any hours over 40 are paid at time and a half
# 2.35
hoursworked = int(input("number of ours worked"))
ratepaid = int(input("pay rate per hour"))
if hoursworked > 40:
    print("it is overtime")
    rateovertime = ratepaid * 1.5
    overtime = (hoursworked - 40) * rateovertime
else:
    if hoursworked == 40:
        print(" it is regularhours")

    else:
        overtime = 0
        regularpay = hoursworked * ratepaid
        finalpayment = regularpay + overtime

    print(finalpayment)





