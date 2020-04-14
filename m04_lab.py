from operator import itemgetter

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
