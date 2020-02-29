#!/usr/bin/python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("name:", name, "  account:", account_no, "    original balance:", "$" \
+ str(balance))

print("")

charge01 = 5.99
charge02 = 12.45
charge03 = 28.05

balance = balance - charge01
print("name:", name, "  account:", account_no, "    charge:", charge01, \
"new balance:", "$" + str(balance))

print("")

balance = balance - charge02
print("name:", name, "  account:", account_no, "    charge", charge02, \
"new balance:", "$" + str(balance))

print("")

balance = balance - charge03
print("name:", name, "  account:", account_no, "    charge", charge03, \
"new balance:", "$" + str(balance))
