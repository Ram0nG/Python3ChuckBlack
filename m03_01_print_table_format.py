#!/usr/bin/Python3

balance = 1000
name = "Tolentino Cala"
account_no = "01123581321"

print("\nName:", name, "    account:", account_no, "    original balance:", "$" + str(balance))

print("\nName:               account      Charge   Balance")
for charge in open("m00_charges-only-file"): #This line open the file that is in the same folder
    balance = balance - float(charge)
    print("{0:16}  {1:10}  {2:8,.2f}  {3:8,.2f}". format(name, account_no, float(charge), balance))
    #the above code {0:16} mean a place on the name variable. 16 mean 16 carateres spaced
    #{1:10} place to account_no and 10 mean 10 carateres spaces
    #{2:8,.2f} same as above here the .2 mean 2 decimal point and f mean float
    # all this is posible because the >>>>>>>.format <<<<<
