file = open('uid.txt')

n = int(input("Nhap vao so dong! \n"))
check = 1
while check == 1:
    lst = []
    for i in range(n):
        line = file.readline().rstrip('\n')
        if line == '':
            check = 0
            break
        else:
            lst.append(line)
    print(lst)
file.close()

