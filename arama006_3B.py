# CSci 1133-20 HW 3
# Haron Arama
# HW 3, Problem 3B

def savingChange(savings, increase, withdraw):
    new_savings = savings * (1.0 + increase) - withdraw
    return new_savings


savings = float("{0:.2f}".format(float(input("Input original savings: "))))
increase = float("{0:.2f}".format(float(input("Input yearly increase: "))))
withdraw = float("{0:.2f}".format(float(input("Input yearly withdraw: "))))
years = int(input("Input number of years: "))

if years >= 1:
    i = 1
    while i <= years:
        savings = float("{0:.2f}".format(savingChange(savings, increase, withdraw)))
        if savings >= 0:
            print("Year: ", i, "Amount: $ ", savings)
        elif savings < 0:
            break
        i += 1

    if savings < 0:
        print("Savings depleted during year ", i)
else:
    print("Invalid time input: ", years)