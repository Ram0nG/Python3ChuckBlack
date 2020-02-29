#! Python3
print("")
print("---- People ----------------------------------------------------------")

person_no = 1
with open("m02_lab_file", "r") as lab_people: # This line will open and Close
                                              # the program

    for people_file in lab_people: # This is the loop

        print(person_no, "  name:", people_file.strip())
        person_no += 1 # This line will increment the numbers on the output

print("")
print("Total People: ", person_no-1)
