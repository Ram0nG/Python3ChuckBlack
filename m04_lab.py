from operator import itemgetter
name = "Name"
location = "Location"
status = "Status"
employer = "Employer"
job = "Job"


print("========================= Unsorted Profiles =========================")

name_list = list()
name_dic = dict()

for name_string in open("m04_lab_profiles.txt"):
    name_info_list = name_string.strip() .split(',')

    name_info = dict()
    name_info['Name'] = name_info_list = [0]
    name_info['Location'] = name_info_list = [1]
    name_info['Status'] = name_info_list = [2]
    name_info['Employer'] = name_info_list = [3]
    name_info['Job'] = name_info_list = [4]

    name_list.append(name_info)

    if name_info['Name'] not in name_dic:
        name_dic[name_info['Name']] = list()

    name_dic[name_info['Name']] .append(name_info)

name_sorted_by_data = sorted(name_list, key=itemgetter('Employer'))

print("\n")
print(" Name       Location       Status         Employer         Job")
print("----------- -------------- -------------- --------------- -----------")

for name, name_info_list in name_dic.items() :

    for name_info in name_info_list:

        print("{0:24}      {1:10}      {2:8}       {3:8}       {4:10}").format(name_info['Name'],
                                                                               name_info['Location'],
                                                                               name_info['Status'],
                                                                               name_info['Employer'],
                                                                               name_info['Job'])

    print('---')

while True:

    name_to_find = input('\n\nEnter Name to find:   ')
    if len(name_to_find) == 0:
        break

    if name_to_find not in name_dic:
        print('Name {} not found'.format(name_to_find))
        continue

    print("\n")
    print(" Name       Location       Status         Employer         Job")
    print("----------- -------------- -------------- --------------- -----------")
    for name_info in name_dic[name_to_find]:

        print("{0:24}      {1:10}      {2:8}       {3:8}       {4:10}").format(name_info['Name'],
                                                                               name_info['Location'],
                                                                               name_info['Status'],
                                                                               name_info['Employer'],
                                                                               name_info['Job'])
Print('\n\n----- Exiting search, Program complete')
exit()
