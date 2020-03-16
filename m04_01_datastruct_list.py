balance = 1000.00
name = "Tolentino Cala"
account_no = "01123581221"

print("name:", name, "      account:", account_no, "    original balance:", "$" + str(balance))

charge_list = []
for charge_string in open ("m00_charges-file"): # Everyline in the file is going to be called charge_string
    charge_info = charge_string.strip() .split(",") # This line is going to format the lines in the file striping the space and adding space everyting separated by comma
    charge_list.append(charge_info) # This will be at list of list

print("\n")
print("Vendor                    Date                charge             Balance")
print("-------------------      ---------------     -----------------   --------")
for charge_info in charge_list:
    balance =  balance - float(charge_info[2])
    print("{0:24}    {1:10}    {2:8,.2f}   {3:20,.2f}".format(charge_info[0],
                                                             charge_info[1],
                                                             float(charge_info[2]),
                                                             balance))
# This is a list of list, this is no the best way to do code
# in the next example he will show how to do the best practice.
