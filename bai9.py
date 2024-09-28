# Lớp Đa Giác
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
    
    def display(self):
        print(f"Đa giác có {self.so_canh} cạnh")

# Lớp Hình Bình Hành kế thừa từ Đa Giác
class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b, chieu_cao):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.chieu_cao = chieu_cao
    
    def tinh_chu_vi(self):
        return 2 * (self.canh_a + self.canh_b)
    
    def tinh_dien_tich(self):
        return self.canh_a * self.chieu_cao

    def display(self):
        print(f"Hình bình hành với các cạnh a = {self.canh_a}, b = {self.canh_b}, và chiều cao h = {self.chieu_cao}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Lớp Hình Chữ Nhật kế thừa từ Hình Bình Hành
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, canh_a, canh_b):
        super().__init__(canh_a, canh_b, canh_b)  # Hình chữ nhật có chiều cao = cạnh b
    
    def display(self):
        print(f"Hình chữ nhật với cạnh dài a = {self.canh_a}, cạnh ngắn b = {self.canh_b}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Lớp Hình Vuông kế thừa từ Hình Chữ Nhật
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
    
    def display(self):
        print(f"Hình vuông với cạnh a = {self.canh_a}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

# Khởi tạo và hiển thị thông tin
hinh_binh_hanh = HinhBinhHanh(5, 3, 4)
hinh_binh_hanh.display()

hinh_chu_nhat = HinhChuNhat(4, 2)
hinh_chu_nhat.display()

hinh_vuong = HinhVuong(3)
hinh_vuong.display()
