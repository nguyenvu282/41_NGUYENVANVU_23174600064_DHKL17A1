class xehoi:
    # KHỞI TẠO INIT KHỞI TẠO ĐỐI TƯỢNG VỚI CÁC THUỘC TÍNH
    def __init__(self,ten,mau,nam_san_xuat):
        self.ten = ten 
        self.mau= mau
        self.nam_san_xuat = nam_san_xuat
        # PHƯƠNG THỨC ĐỂ IN THÔNG TIN XE
    def hienthixehoi(self):
        print(f"tên xe {self.ten}")
        print(f"màu xe {self.mau}")
        print(f"nam sản xuất  {self.nam_san_xuat}")
        # PHƯƠNG THỨC CẬP NHẬP MÀU XE MỚI

    def updetecoler(self,new_coler):
        self.mau = new_coler
        print(f"màu xe mới sau khi cập nhập là màu {self.mau}")

xehoi1 = xehoi("maserati",'đỏ',' 1999')
xehoi2 = xehoi("lamborghini",'vàng','1985')
  

print(" hiển thị thông tin từng xe")
xehoi1.hienthixehoi()
print(" hiển thị thông tin xe sau khi thay đổi")
xehoi1.updetecoler("redflag")