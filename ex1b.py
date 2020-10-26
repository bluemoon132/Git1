set_student1 = {"luu thanh dat", "20184061", "gold"}
set_student2 = {"nguyen van dai", "20189182", "challenge"}
set_work = {"nguyen van dai", "gold"}

print(set_student1)

set_student1.add("IT-E6")
print(set_student1)

set_student1.remove("gold")
print(set_student1)     

print(set_student2)
print(set_work,'\n')

print( set_work | set_student2)
