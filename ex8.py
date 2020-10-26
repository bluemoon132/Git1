def sum(a, b):
    return a / b


try:
    print(sum(6, 0))
except ZeroDivisionError:
    print('Co loi xay ra!')


try:
  print(age)
except NameError:
  print("Bien age chua duoc dinh nghia")
except:
  print("Co loi xay ra trong chuong trinh !")


try:
  age = 5
  print("age = " + age)
except NameError:
  print("Bien age chua duoc dinh nghia")
except:
  print("Co loi xay ra trong chuong trinh")