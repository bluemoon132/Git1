import re


class Find_phone_number:
    def __init__(self):
        self.strin = "hello day 096 678 7645  là 10000000  cua em 2019 0936548873 - 0947655443 va (+84)928964755 " \
                     "va so 1900 1098 nay nua 1900.1096 th 0298.8964.731 va 058 399 998  098 767 7875 h la " \
                     "(024)357-9231 them nua 049757335272  0454872592 va +8423465453 "

    def replace_zero(self):
        for i in range(len(self.strin)):
            self.strin = self.strin.replace("(+84)", "0")
            self.strin = self.strin.replace("(024)", "024")
            self.strin = self.strin.replace("+84", "0")
            self.strin = self.strin.replace("-", "")
            self.strin = self.strin.replace(".", " ")
        # print(self.strin)
        return self

    def find(self):
        s = re.findall(r'[0]{1}\d{8,9}', self.strin) + re.findall(r'[0]{1}\d{2,}\s\d{3,}\s\d{3,}',
                                        self.strin) + re.findall(r'[1]{1}\d{3,4}\s\d{4,5}',self.strin)
        # s = re.findall(r'')
        print(s)


find = Find_phone_number()
find.__init__()
find.replace_zero()
find.find()
