balance = 1000
name = "Tolention Cala"
account_no = "01123581321"

print("\nName:", name,  "   Account:", account_no, "    original balance:", "$" + str(balance))

charges_file = open("m00_charges-file") # Chuck called this the old school way of open a file
for charge_info_string in charges_file:
    charge_info = charge_info_string.strip() .split(',') # the .strip off or remove the space format of the file
    print(charge_info)                     # from the begining and the end of the file.
                                       # and the .split is a comma separated value explited into a list
