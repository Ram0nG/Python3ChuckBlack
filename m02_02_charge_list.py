#!usr/bin/python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("name:", name, "  account:", account_no, "original balance:", "$" +\
str(balance))

charges = [5.99, 12.45, 28.05]

balance = balance - charges[0]
print("name:", name, "  account:", account_no, "charges:", charges[0], "   new balance:", "$" + str(balance))
balance = balance - charges[1]
print("name:", name, "  account:", account_no, "charges:", charges[1], "   new balance:", "$" + str(balance))
balance = balance - charges[2]
print("name:", name, "  account:", account_no, "charges:", charges[2], "   new balance:", "$" + str(balance))
