#khoi tao class
#class <tenlop> ():
class item():
    def __init__(self,ten:str,gia,soluong:int):# khai bao thuoc tinh dac trung và muốn kiểu dữ liệu cụ thể
        self.ten= ten
        self.gia = gia
        self.soluong=soluong
        assert gia >= 0 and soluong >= 0 # kiểm tra điều kiện thuộc tính
    def tonggia(self):
        return self.gia*self.soluong    #method #  là các hàm đc định  nghĩa bên trong 1 class , các hàm này đc sử dụng 1 số cv cụ thể

#phương thức tĩnh  ; là 1 phương thức tiện ích chung thực hiện 1 tác vụ riêng lẻ
    @staticmethod
    def checkgia(gia):
        if gia < 500:
            return " hàng cấp thấp"
        else:
            return " hàng expensive"
# Khởi tạo class con 
# Tính kế thừa : tạo ra 1 thằng con dc thừa hưởng toàn bộ từ thằng cha thêm các thuộc tính từ thằng con
class phone(item):
    def __init__ (self,ten:str,gia,soluong:int,loai= " ios 18"):
        super().__init__(
            ten,gia,soluong
            

        )  # 1 hàm duy nhất khai báo toàn bộ thuộc tính thằng cha
        self.loai = loai
        
    
# doi tuong cu the
item1 = item("samsung",499,3)
# method
print(item1.tonggia())
print(item.checkgia(499))
# thử class con 
phone1 = phone("ip 16",2000,100,"ios18")
print(phone1.gia)



