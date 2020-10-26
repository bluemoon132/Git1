class Tong_3_so:
    def sum(self, n, lst):
        for i in range(0, n):
            for j in range(i, n):
                for k in range(j, n):
                    if lst[i] + lst[j] + lst[k] == 0 and lst[i] != lst[j] and lst[i] != lst[k] and lst[j] != lst[k]:
                        print("Cac phan tu do la", lst[i], lst[j], lst[k])

print("Nhap vao so phan tu cho day!")
n = int(input())
lst = []
for i in range(n):
    lst.append(float(input()))

sum = Tong_3_so()
sum.sum(n, lst)
