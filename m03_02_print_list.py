balance = 1000
name = "Tolention Cala"
account_no = "01123581321"

print("\nName:", name,  "   Account:", account_no, "    original balance:", "$" + str(balance))

charges_file = open("m00_charges-file")
for charge_info_string in charges_file:
    charge_info = charge_info_string.strip() .split(',')
    print(charge_info)
