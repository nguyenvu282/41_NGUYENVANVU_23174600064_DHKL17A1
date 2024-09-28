class monhoc:
    def __init__(self,mamh,tenmh,sotc):
        self.mamh=mamh
        self.tenmh=tenmh
        self.sotc=sotc

    def hienthimh(self):
        print(" mamh :" , self.mamh)
        print("tenmh:", self.tenmh)
        print("sotc :", self.sotc)

dsmh = []
def nhapds():
    n = int(input(" nhap so luong danh  sach mon hoc:"))
    for i in range(n): 
        print(" nhap danh sach thu", i+1 )
        mamh = int(input(" nhap ma mh:"))
        tenmh = input(" nhap ten mon hoc:")
        sotc = int(input(" nhap so tinh chi:"))
        mh = monhoc(mamh, tenmh,sotc)
        dsmh.append(mh)

def hienthidsmh():
    print(" danh sach mon hoc la:")
    for i in range(len(dsmh)):
        print(" thong tin mon hoc", i+1 )
        dsmh[i].hienthimh()


def themmh():
    print(" nhap thong tin mon hoc can them ")
    mamh = int(input("nhap ma mon hoc moi :"))
    tenmh = input(" nhap ten monn hoc:")
    sotc = int(input(" nhap so tin chi:"))
    mh = monhoc(mamh,tenmh,sotc)
    dsmh.append(mh)
def xoamh(maxoa):
    for mh in dsmh:
        if (mh.mamh == maxoa):
            dsmh.remove(mh)
def timkiem(thongtin):
    for i in range (len(dsmh)):
        if (dsmh[i].mamh == thongtin or dsmh[i].tenmh == thongtin or dsmh[i].sotc == thongtin):
            dsmh[i].hienthimh()







def main():
    nhapds()
    hienthidsmh()
    #maxoa = int(input(" xoa mon hoc theo ma"))
    #xoamh(maxoa)
    #print(maxoa)
    #hienthidsmh()
    thongtin = input(" nhap vao th0ng tin ban can tim kiem")
    timkiem(thongtin)
    



main()             
                   