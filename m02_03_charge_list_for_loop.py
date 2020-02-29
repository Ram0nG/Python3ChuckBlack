#!/usr/bin/python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("name:", name, "  account:", account_no, " original balance:", "$" + str(balance))

charges = [5.99, 12.45, 28.05] # This is a list

for charge in charges: # This for loop will make the program better and it will reference the list above
    balance = balance - charge
    print("name:", name, "  account:", account_no, "    charge:", charge, " new balance:", "$" + str(balance))
