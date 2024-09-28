#Kiểu dữ liệu danh sách list
#b = [1,2,4,6,7,5,4]
# them vao cuoi ptu
#b.append(6)
# them vào vị trí bất kì(vị trí muốn thêm và giá trị muốn thêm)
#b.insert(2,9)
# xóa phân tủ trong danh sách
#b.__delitem__(-1)
# xóa gtri có trong danh sách nếu có giá trị lặp thì chỉ xóa gia trị đầu tiên
#b.remove(1)
#print(b)
# nhập danh sách từ bàn phím , khởi tạo 1 danh sách rỗng
a = []
n = int(input(" nhap n = "))
for i in range(n):
    print("nhập phần tử thứ " , i +1,"là:")            
    x = int(input())
    a.append(x)
    
print(a) 

b = sorted(a) # sắp xếp tăng dần # giảm dần thêm sorted(reverse=true)
print(b)
