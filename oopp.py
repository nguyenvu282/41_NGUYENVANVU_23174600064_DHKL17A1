class sinhvien():
    def __init__(self,hoten,que,lop,diempy,tkweb):
        self.hoten = hoten
        self.que=que
        self.lop = lop
        self.diempy=diempy
        self.tkweb=tkweb

    def diemtb(self):
        dtb = (self.diempy*4+self.tkweb*3)/2
        return dtb
      
    def xeploai(self,dtb):
        if (dtb<5):
            print('yeu')
        elif (5<=dtb<7):
            print("tb")
        elif(7<=dtb<8):
            print("kha")
        elif(8<=dtb<9):
            print("gioi")
        else:
            print("xuat sac")

# tao ra 1 doi tuong sinh vien cu the
sv1 = sinhvien("vu","hduong","17a1",9,9 )
print(sv1.diemtb())
print(sv1.xeploai(sv1.diemtb()))

        