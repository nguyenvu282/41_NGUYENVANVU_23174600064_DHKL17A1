class bank():
    def __init__(self, hoten ,cmt):
        self.hoten = hoten
        self.cmt = cmt

class nhanvien(bank):
    def __init__(self, hoten, cmt):
        super().__init__(
            hoten,cmt
        )
        self.__luong = 50000
    def get_luong(self):
        return self.__luong
    def set_luong(self,luong_moi):
        self.__luong = luong_moi

    

nv2 = nhanvien("trang",4376282344)
nv2.set_luong(99999999)
print(nv2.get_luong())  


