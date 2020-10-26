import re


class Html_em:
    def __int__(self):
        self.s1 = "Xin chào <em>đồng chí</em>, đồng chí <em>yếu đuối</em> quá"

    def output(self):
        s = re.findall(r"<em>(.*?)</em>", self.s1)
        print(s)


str2 = Html_em()
str2.__int__()
str2.output()
