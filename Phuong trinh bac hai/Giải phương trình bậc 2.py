#Đưa thư viện Math vào code
import math

#In đề bài
print("Giải phương trình bậc hai ax^2 + bx + c = 0")

#Nhập từ bàn phím 3 số a, b, c
a = float(input("a = "))
while True:
    if a != 0:
        break
    else:
        a = float(input("a khác 0, nhập lại a: "))
b = float(input("b = "))
c = float(input("c = "))

#Tính delta
Delta = b**2 - 4*a*c

#Giải phương trình
if Delta > 0:
    x1 = (-b+Delta)/2*a
    x2 = (-b-Delta)/2*a
    print("Phương trình có 2 nghiệm phân biệt x1 = ", x1, "x2 = ", x2)
if Delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -b/2*a)
else:
    print("Phương trình vô nghiệm")