# write a function that takes two parameters- a pay rate and
# the number of hours worked- and returns the pay. any hours over 40 are paid at time and a half
# 2.35
def income(payrate, hoursworked):
    if hoursworked <= 40:
        regularpay = hoursworked * payrate
        finalpayment = regularpay

    else:
            regularpay = 40 * payrate
            overtimerate = (hoursworked - 40) * (1.5 * payrate)
            finalpayment = regularpay + overtimerate



    print("finalpayment", finalpayment)
    return finalpayment


income(10, 50)
income(10, 30)
