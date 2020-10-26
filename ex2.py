def remove_space(str3):
    p = str3.index(" ")
    str3 = str3[p+1:]
    return str3
def remove_last(str3):
    str3 = str3[:len(str3)-1]
    return str3
stri = "<meta property=\"og:image\" itemprop=\"thumbnailUrl\" content=\"https://s1.vnecdn.net/vnexpress/restruct/i/v341/logo_default.jpg\">"
str1 = input()
str2 = stri.split("\"")
lst = []
count = 0
for str3 in str2:
    if str3[-1] == "=" :
        str3 = remove_space(str3)
        str3 = remove_last(str3)
        lst.append(str3)
        count += 1
    else:
        lst.append(str3)
        count += 1

# print(lst)
check = 0
for i in range(0,count-1):
    if str1 == lst[i]:
        print(lst[i+1])
        check = 1
        break
if check == 0:
    print("The word '" + str1 + "' is not in string")

