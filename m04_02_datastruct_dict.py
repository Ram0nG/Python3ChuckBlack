balance = 1000.00
name = "Tolention Cala"
account_no = "01123581221"

print("name:", name, "  account:", account_no, "   original balance:", "$" + str(balance))

charges_list = []
for charge_string in open("m00_charges-file"):
    charge_info_list = charge_string.strip() .split(",")

    charge_info = dict()
    charge_info ['vendor'] = charge_info_list[0]
    charge_info ['date'] = charge_info_list[1]
    charge_info ['charge'] = charge_info_list[2]

    charges_list.append(charge_info)

print("\n")
print("Vendor                    Date                charge               Balance")
print("-------------------      ---------------     -----------------     --------")
for charge_info in charges_list:
    balance = balance - float(charge_info['charge'])
    print("{0:24}   {1:10}    {2:12,.2f}   {3:20,.2f}".format(charge_info['vendor'],
                                                            charge_info['date'],
                                                            float(charge_info['charge']),
                                                            balance))
