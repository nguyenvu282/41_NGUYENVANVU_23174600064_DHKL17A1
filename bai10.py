# Lớp Điểm (Diem)
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

# Lớp Elip thừa kế từ Diem
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y)  # Gọi hàm tạo của lớp Diem
        self.ban_truc_lon = ban_truc_lon  # Bán trục lớn (a)
        self.ban_truc_nho = ban_truc_nho  # Bán trục nhỏ (b)
    
    def tinh_dien_tich(self):
        # Công thức tính diện tích elip: S = pi * a * b
        import math
        return math.pi * self.ban_truc_lon * self.ban_truc_nho
    
    def display(self):
        super().display()  # Hiển thị tọa độ của điểm
        print(f"Elip với bán trục lớn: {self.ban_truc_lon} và bán trục nhỏ: {self.ban_truc_nho}")
        print(f"Diện tích elip: {self.tinh_dien_tich()}")

# Lớp Đường tròn thừa kế từ Elip
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  # Đường tròn có bán kính là bán trục lớn = bán trục nhỏ

    def display(self):
        super().display()  # Hiển thị thông tin elip (thực chất là đường tròn)
        print(f"Đường tròn với bán kính: {self.ban_truc_lon}")  # Bán trục lớn chính là bán kính

# Nhập dữ liệu và sử dụng
x = float(input("Nhập tọa độ x của điểm tâm elip: "))
y = float(input("Nhập tọa độ y của điểm tâm elip: "))
ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))

elip = Elip(x, y, ban_truc_lon, ban_truc_nho)
elip.display()

# Ví dụ về đường tròn
ban_kinh = float(input("Nhập bán kính đường tròn: "))
duong_tron = DuongTron(x, y, ban_kinh)
duong_tron.display()
