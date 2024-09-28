# tính bao đóng (encapsulation) sẽ luôn có các thuộc tính mà ta luôn cố định nó ,điều này ngăn chặn dữ liệu bị sửa dổi tt
class banking():
    def __init__(self,hoten,cmt):
        self.hoten = hoten
        self.cmt = cmt

class nhanvien(banking):
    def __init__(self,hoten,cmt):
        super().__init__(
            hoten,cmt
        )        
        self.__luong = 5000 # sử dụng private o cho phép truy cập từ bên ngoài
        #code để người có thẩm quyền can thiệp vào lương
        def get_luong(self): # lấy lương ra
            return self.__luong
        def set_luong(self,luongmoi):
            self.__luong = luongmoi
        
            
 
nv1 = nhanvien("trang anh",'437583')
#print(nv1.cmt,nv1.hoten,nv1.luong)
#nv1.luong = 457845637 # public có thể can thiệp tt và sửa lowng của nhân viên
nv1.set_luong(9999999)
print(nv1.get_luong())
