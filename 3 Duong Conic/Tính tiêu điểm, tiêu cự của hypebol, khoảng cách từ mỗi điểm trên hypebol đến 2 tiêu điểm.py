#Đưa thư viện Math vào code
import math

print("Tìm tiêu điểm, tiêu cự của phương trình chính tắc hypebol (x^2/a^2) - (y^2/b^2) = 1")

#Nhập từ bàn phím 2 số a và b
a = float(input("a = "))

while True:
    if a > 0:
        break
    else:
        a = float(input("a > 0, nhập lại số a: "))

b = float(input("b = "))
while True:
    if b > 0:
        break
    else:
        b = float(input("b > 0, nhập lại số b: "))

#Tính c
c = math.sqrt(a**2 + b**2)
        
#Tính 2 tiêu điểm
xf1 = -(math.sqrt(a**2 + b**2))
xf2 = math.sqrt(a**2 + b**2)
print("Tiêu điểm f1 (", xf1, "0)")
print("Tiêu điểm f2 (", xf2, "0)")

#Tính tiêu cự
f1f2 = 2*c
print("Tiêu cự f1f2 = ", f1f2)

#Tính tổng khoảng cách từ mỗi điểm trên hypebol đến 2 tiêu điểm
m = 2*a
print("Tổng khoảng cách |MF1+MF2| = ", m)

