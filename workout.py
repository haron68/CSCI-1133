change = float(input("Input an amount between 1 and 99 cents: "))

Quarter = change // 25
change -= Quarter * 25
Dime = change % 25 // 10
change -= Dime * 10
Nickel = change % 25 % 10 // 5
change -= Nickel * 5
Penny = change % 25 % 10 % 5

print("Quarter: ", Quarter, "Dime: ", Dime, "Nickel: ", Nickel, "Penny: ", Penny)