#!/usr/bin/Python3

balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("\nName:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

charge_file = open("m00_charges-file")
for charge_info_string in charge_file:
    charge_info = charge_info_string.strip().split(',')
    print(charge_info)
