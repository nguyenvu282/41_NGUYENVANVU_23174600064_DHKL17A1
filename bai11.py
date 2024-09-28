import math

# Lớp TamGiac
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh a
        self.b = b  # Cạnh b
        self.c = c  # Cạnh c
    
    def kiem_tra_tam_giac(self):
        # Kiểm tra điều kiện để là tam giác
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    def tinh_dien_tich(self):
        # Dùng công thức Heron
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def display(self):
        print(f"Các cạnh tam giác: a={self.a}, b={self.b}, c={self.c}")
        if self.kiem_tra_tam_giac():
            print(f"Chu vi: {self.tinh_chu_vi()}")
            print(f"Diện tích: {self.tinh_dien_tich()}")
        else:
            print("Ba cạnh không tạo thành tam giác.")

# Lớp TamGiacCan (thừa kế từ TamGiac)
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        super().__init__(canh_bang, canh_bang, canh_khac)  # Tam giác cân có 2 cạnh bằng nhau

    def display(self):
        print(f"Tam giác cân với cạnh bằng nhau: a=b={self.a}, cạnh khác: c={self.c}")
        super().display()

# Lớp TamGiacDeu (thừa kế từ TamGiacCan)
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)  # Tam giác đều có 3 cạnh bằng nhau

    def display(self):
        print(f"Tam giác đều với các cạnh a=b=c={self.a}")
        super().display()

# Lớp TamGiacVuong (thừa kế từ TamGiac)
class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)  # Cạnh huyền theo định lý Pythagore
        super().__init__(a, b, c)

    def display(self):
        print(f"Tam giác vuông với hai cạnh góc vuông a={self.a}, b={self.b}, cạnh huyền c={self.c}")
        super().display()


# Sử dụng các lớp trên
# Tạo tam giác thường
a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
tam_giac = TamGiac(a, b, c)
tam_giac.display()

# Tạo tam giác cân
canh_bang = float(input("\nNhập cạnh bằng nhau của tam giác cân: "))
canh_khac = float(input("Nhập cạnh khác của tam giác cân: "))
tam_giac_can = TamGiacCan(canh_bang, canh_khac)
tam_giac_can.display()

# Tạo tam giác đều
canh_deu = float(input("\nNhập cạnh của tam giác đều: "))
tam_giac_deu = TamGiacDeu(canh_deu)
tam_giac_deu.display()

# Tạo tam giác vuông
a_vuong = float(input("\nNhập cạnh góc vuông a của tam giác vuông: "))
b_vuong = float(input("Nhập cạnh góc vuông b của tam giác vuông: "))
tam_giac_vuong = TamGiacVuong(a_vuong, b_vuong)
tam_giac_vuong.display()
