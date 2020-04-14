from operator import itemgetter

name_list = []
for name_string in open ("m04_lab_profiles.txt"):
    name_info_list = name_string.strip() .split(',')

    name_info = dict()
    name_info['name'] = name_info_list[0]
    name_info['location'] = name_info_list[1]
    name_info['status'] = name_info_list[2]
    name_info['employer'] = name_info_list[3]
    name_info['job'] = name_info_list[4]

    name_list.append(name_info)

print("\n")
print("name                         location                   Status                Employer                       Job")
print("----------------------------------------------------------------------------------------------------------------")
for name_info in name_list:
    print("{0:24}      {1:20}      {2:10}       {3:15}       {4:15}").format(name_info['name'],
                                                                           name_info['location'],
                                                                           name_info['status'],
                                                                           name_info['employer'],
                                                                           name_info['job'])

name_sorted_by_data = sorted(name_list, key=itemgetter('location'))

print("\n")
print("name                         location                   Status                Employer                       Job")
print("----------------------------------------------------------------------------------------------------------------")
for name_info in name_sorted_by_data:
    print("{0:24}      {1:10}      {2:10}       {3:15}       {4:10}").format(name_info['name'],
                                                                           name_info['location'],
                                                                           name_info['status'],
                                                                           name_info['employer'],
                                                                           name_info['job'])
