
# List Port#, Patch#, Switch Location, Date added
# String with comma-separated names, addresses, cities, phones
# Print tabular information about all Network Info
# Extra Cedit: read information from file.



Salami_House = ['tw/1/1/1','B46','Salami House', '3/12/20']
Prov_loc = ['te2/1/1', 'C33', 'Prov Location', '2/14/20']
Frezee_string = '1:1,D48,Freeze Closet,1/1/17'
DI_string = 'ge.1.1,A1,RayosX,9/3/19'

print("")
print("Port#                Patch#               Switch             date")
print("------------         -----------        ---------------    ---------\
----")

print("{:18}   {:20}   {:16}   {:15}".format(Salami_House[0],
                                             Salami_House[1],
                                             Salami_House[2],
                                             Salami_House[3]))
print("{:18}   {:20}   {:16}   {:15}".format(Prov_loc[0], # This is the best way to brake the line in
                                             Prov_loc[1], # Small lines
                                             Prov_loc[2],
                                             Prov_loc[3]))
Frezee_list = Frezee_string.split(',')
DI_list = DI_string.split(",")
print("{:18}   {:20}   {:16}   {:15}".format(Frezee_list[0],Frezee_list[1],Frezee_list[2],Frezee_list[3]))
print("{:18}   {:20}   {:16}   {:15}".format(DI_list[0],DI_list[1],DI_list[2],DI_list[3]))
