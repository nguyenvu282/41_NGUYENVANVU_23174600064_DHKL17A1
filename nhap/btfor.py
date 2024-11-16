n = int(input(" nhap so n :"))
tong = 0
dem = 0
while(n!=0):
    i = n % 10
    tong +=i
    n//=10
    dem +=1

print(tong, dem)    

