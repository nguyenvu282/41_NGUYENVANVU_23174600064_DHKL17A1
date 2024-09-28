class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
        self.tong_diem = self.tinh_tong_diem()

    # Phương thức tính tổng điểm
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    # Phương thức hiển thị thông tin thí sinh
    def hien_thi(self):
        print(f"Họ tên: {self.ho_ten}, Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}, Tổng điểm: {self.tong_diem}")

# Nhập danh sách thí sinh
def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    
    for i in range(so_luong):
        ho_ten = input(f"Nhập họ tên thí sinh thứ {i+1}: ")
        diem_toan = float(input(f"Nhập điểm Toán của thí sinh thứ {i+1}: "))
        diem_ly = float(input(f"Nhập điểm Lý của thí sinh thứ {i+1}: "))
        diem_hoa = float(input(f"Nhập điểm Hóa của thí sinh thứ {i+1}: "))
        thi_sinh = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(thi_sinh)
    
    return danh_sach

# Hiển thị danh sách thí sinh trúng tuyển
def hien_thi_trung_tuyen(danh_sach, diem_chuan=20):
    print("\nDanh sách thí sinh trúng tuyển (điểm chuẩn >= 20):")
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tong_diem >= diem_chuan]
    
    # Sắp xếp danh sách theo tổng điểm giảm dần
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tong_diem, reverse=True)
    
    # Hiển thị danh sách trúng tuyển
    for thi_sinh in danh_sach_trung_tuyen:
        thi_sinh.hien_thi()

# Chương trình chính
danh_sach_thi_sinh = nhap_danh_sach_thi_sinh()
hien_thi_trung_tuyen(danh_sach_thi_sinh)

              
           


        


   
                         