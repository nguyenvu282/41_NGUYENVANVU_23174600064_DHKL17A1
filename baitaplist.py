# bài tập 1
#a = [4,2,6,7,9,8]
#b = len(a)
#for i in range(b//2):
    #vu = a[i]
    #a[i] = a[b-1-i]
    #a[b-1-i]=vu

#print(a)    
#bài tập 2 tính giá trị biểu thức a0 +a1*x+a2*x^2 +...+an*xn^n
a = []
n = int(input(" nhập n="))
for i in range(n):
    print("nhập vào phần tử thứ", i+1,"là:")
    x = int(input(" nhập x :"))
    a.append(x)
p = 0
x = int(input("nhập x :"))
for i in range(n):
    p+=a[i]*(x**i)

print("p =",p)
# bài tập 3 nhập doanh sso bán hàng
doanhso = []
n = int(input(" mời nhập số cửa hàng mà bạn muốn:"))
for i in range(n):
    print("nhập doanh số của từng cửa hàng", i+1, "lá:")
    x = int(input())
    doanhso.append(x)

print(doanhso)    
# sắp xếp doanh số cửa hàng tù bé đến lơn
print("sắp xếp doanh số từ bé đến lớn")
doanhso1 = sorted(doanhso)
print(doanhso1)
#tính trung bình doanh so cửa hàng
tongdoanhso = sum(doanhso)
print("doanh số tb của cửa hàng ")
tb = sum(doanhso)/n
print(tb)
#hiện thị doanh số bán hàng lớn nhất
print("doanh số bán hàng lớn nhất ")
dsomax= max(doanhso)
print(dsomax)
#hiện thị doanh sso nhỏ nhất
print("doanh số bé nhất")
dsomin = min(doanhso)
print(dsomin)   

