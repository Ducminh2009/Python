#Đưa thư viện Math vào code
import math

print("Tìm tiêu điểm, đường chuẩn của phương trình chính tắc parabol y^2 = 2px")

#Nhập từ bàn phím p
p = float(input("p = "))
while True:
    if p > 0:
        break
    else:
        p = float(input("p > 0, nhập lại p = "))
        
#Tìm tiêu cự của p
xf = p/2
print("Tiêu điểm p (", xf, "0)")

#Tìm đường chuẩn
x = -(p/2)
print("Đường chuẩn x = ", x)