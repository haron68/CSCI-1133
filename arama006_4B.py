# CSci 1133-20 HW 4
# Haron Arama
# HW 4, Problem 4B

import random

def savingChange(savings, increase, withdraw):
    new_savings = savings * (1.0 + increase) - withdraw
    return new_savings


savings         = float("{0:.2f}".format(float(input("Input original savings: "))))
increase_min    = float("{0:.2f}".format(float(input("Input yearly increase minimum: "))))
increase_max    = float("{0:.2f}".format(float(input("Input yearly increase maximum: "))))
withdraw_min    = float("{0:.2f}".format(float(input("Input yearly withdraw minimum: "))))
withdraw_max    = float("{0:.2f}".format(float(input("Input yearly withdraw maximum: "))))
years           = int(input("Input number of years: "))
trials          = int(input("Input number of trials: "))

initial         = savings
if years >= 1 and trials >= 1:
    t = 1
    fail = 0
    while t <= trials:
        increase = random.uniform(increase_min, increase_max)
        withdraw = random.uniform(withdraw_min, withdraw_max)
        savings = initial
        i = 1
        while i <= years:
            savings = float("{0:.2f}".format(savingChange(savings, increase, withdraw)))
            if savings < 0:
                fail += 1
                success = float("{0:.2f}".format(((trials - fail) / trials) * 100))
                break
            else:
                success = float("{0:.2f}".format(((trials - fail) / trials) * 100))
            i += 1
        t += 1

    print("Success percentage: ", success, " %")
else:
    print("Invalid time and or trial count input: ", years, trials)