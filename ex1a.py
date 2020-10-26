dict_student = {
    "id" : 20184061,
    "name" : "luu thanh dat",
    "class" : "VN04",
    "rank" : 'gold'
}

for x in dict_student:
    print(x, ": ", dict_student.get(x))
print('\n')

dict_student["class"] = "IT-E6"
for x in dict_student:
    print(x, ": ", dict_student.get(x))
print('\n')

dict_student.pop("rank")
for x in dict_student:
    print(x, ": ", dict_student.get(x))