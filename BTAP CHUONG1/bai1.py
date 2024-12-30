class Hinh_cn:
    def __init__(self):
        self.dai=0.0
        self.rong=0.0
    def nhap_tt(self):
        self.dai=float(input('Chieu dai='))
        self.rong=float(input('Chieu rong= '))
    def tinh_toan(self):
        print('Chieu dai:',self.dai)
        print('Chieu rong:',self.rong)
        print('Chu vi HCN {}'.format((self.dai+self.rong)/2))
        print('Dien tich HCN {}'.format(self.dai*self.rong))
obj=Hinh_cn()
obj.nhap_tt()
obj.tinh_toan()