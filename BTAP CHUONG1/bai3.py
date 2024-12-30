class PS:
    def __init__(self,tu_so,mau_so):
        self.tu_so=tu_so
        self.mau_so=mau_so
    def kiem_tra(self):
        if tu_so.is_integer()==True and tu_so.is_integer()==True and int(self.tu_so) != 0 :
            print('Phân số hợp lệ !! ')
            print('Phân số : {}/{}'.format(int(self.tu_so),int(self.mau_so)))
        else:
            print('Phân số không hợp lệ')
tu_so=float(input('Tử số = '))
mau_so=float(input('Mẫu số = '))
obj=PS(tu_so,mau_so)
obj.kiem_tra()