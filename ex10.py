import random


class List_random:
    def __init__(self):
        self.lst = [c for c in range(100, 201)]

    def random(self):
        lst1 = []
        num = 0
        while len(lst1) < 5:
            num = random.choice(self.lst)
            if num % 3 == 0 and num not in lst1 and num > 99 and num < 201:
                lst1.append(num)
        return lst1


# lst = List_random()
# lst.__init__()
# print(lst.random())


class Number_only:
    def __int__(self):
        self.strin = "Tôi từng tự ý bán cả danh mục 20-30 mã cổ phiếu của một chị khách rất thân quen trong năm 2007 và bị cằn nhằn không dứt, may là tình chị em vẫn còn sau đợt khủng hoảng đó. "
        self.lst = []

    def number(self):
        strsplit = []
        for strsplit1 in self.strin.split("-"):
            strsplit += strsplit1.split(" ")

        for strtest in strsplit:
            check = 0
            for i in range(0, len(strtest)):
                if "0" <= strtest[i] <= "9":
                    check = 1
                else:
                    check = 0
                    break
            if check == 1:
                self.lst.append(strtest)
        return self.lst


num = Number_only()
num.__int__()
print(num.number())
