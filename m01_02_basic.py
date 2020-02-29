#!/usr/bin/python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581231"

print("name:", name, "account:", account_no, "balance:", balance)
print("name:", name, "account:", account_no, "balance:", "$" + str(balance))
print("name:", name, "account:", account_no, "balance:", "$" + str(float(balance)))

print("\n")

balance = 1000.00
new_balance = balance
balance += 250
print("balance object id:    ", id(balance), "balance value: ", balance)
print("new balance object id:", id(balance), "new_balance value:", new_balance)
