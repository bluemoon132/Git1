from datetime import datetime
strtime = "thứ hai, 20 tháng 7 năm 2020 10:37:06 GMT+07:00"
strsplit = strtime.split(" ")
lst = []
print(strsplit)

for strtest in strsplit:
    check = 1
    for i in range (0, len(strtest)):
        if strtest[i] >= "a" and strtest[i] <= "z":
            check = 0
            break
        elif strtest[i] >= "A" and strtest[i] <= "Z":
            check = 0
            break
    if check == 1:
        lst.append(strtest)
print(lst)

strtimeee = "".join(lst)
# print(lst)
print(strtimeee)

# Định dạng ở dạng ddmmyyyyHHMMSS
dt_object1 = datetime.strptime(strtimeee, "%d%m%Y%H:%M:%S")
print(dt_object1)

timestamp = datetime.timestamp(dt_object1)
print(timestamp)