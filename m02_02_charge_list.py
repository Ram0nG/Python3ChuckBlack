#!/usr/bin/python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("name:", name, "  account:", account_no, "original balance:", "$" +\
str(balance)) # This line is calling the Variables above

charges = [5.99, 12.45, 28.05] # This is a list that will be reference in the code below

balance = balance - charges[0] # This reference 5.99 in the list
print("name:", name, "  account:", account_no, "charges:", charges[0], "   new balance:", "$" + str(balance))
balance = balance - charges[1] # This reference 12.45 in the list
print("name:", name, "  account:", account_no, "charges:", charges[1], "   new balance:", "$" + str(balance))
balance = balance - charges[2] # This reference 28.95 in the list
print("name:", name, "  account:", account_no, "charges:", charges[2], "   new balance:", "$" + str(balance))
