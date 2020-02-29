#! python3
balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581321"

print("name:", name, "  account:", account_no, "original balance:", "$" + str(balance))

charges_file = open("m00_charges-only-file")
for charge in charges_file:
    balance = balance - float(charge) # need to let python know that the file cointain a float, if not python will take it as string
    print("name:", name, "  account:", account_no), "   charge:", charge.strip(), " new balance:", "$" + str(balance)
