
# List with People names, address, citiers, phones
# String with comma-separated names, addresses, cities, phones
# Print tabular information avbout all people
# Extra Cedit: read information from file.



fred_list = ['Fred Flinstone','1232 Granite Drive','Bedrock CA', '916.555.0000']
barney_list = ['Barney Rubble', '1246 Lava Court', 'Bedrock CA', '916.555.111']
wilma_string = 'Wilma Flinstone,1234 Granite Drive,Bedrock CA,916.555.0101'
dino_string = 'Dino,1234 Granite Drive,Bedrock CA,n/a'

print("")
print("Name                 Address                City               Phone")
print("------------         --------------         ---------------    ---------\
----")

print("{:18}   {:20}   {:16}   {:15}".format(fred_list[0],fred_list[1],fred_list[2],fred_list[3]))
print("{:18}   {:20}   {:16}   {:15}".format(barney_list[0], # This is the best way to brake the line in
                                             barney_list[1], # Small lines
                                             barney_list[2],
                                             barney_list[3]))
dino_list = dino_string.split(",")
wilma_list = wilma_string.split(',')
print("{:18}   {:20}   {:16}   {:15}".format(wilma_list[0],wilma_list[1],wilma_list[2],wilma_list[3]))
print("{:18}   {:20}   {:16}   {:15}".format(dino_list[0],dino_list[1],dino_list[2],dino_list[3]))
