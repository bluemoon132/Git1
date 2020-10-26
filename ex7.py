import math


class Polygon:
    def __init__(self, number):
        self.socanh = number
        self.lst_edge = []

    def add_edge(self):
        for i in range(self.socanh):
            self.lst_edge.append(float(input()))

    def print_edge(self):
        for i in self.lst_edge:
            print(i)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def circumference(self):
        a, b, c = self.lst_edge
        sum1 = a + b + c
        return sum1

    @property
    def area(self):
        a, b, c = self.lst_edge
        p = (a + b + c) / 2
        area1 = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area1


tamgiac = Triangle()
tamgiac.add_edge()
tamgiac.print_edge()
print("Circumference is:", tamgiac.circumference())
print("Area is:", tamgiac.area)
