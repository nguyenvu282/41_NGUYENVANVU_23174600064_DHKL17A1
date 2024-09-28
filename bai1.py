class HCN:
    def __init__(self,dai, rong):
        self.dai=dai
        self.rong=rong
    def hienthitthcn(self):
        print(f"chiều dài HCN là {self.dai}")
        print(f"chiều rộng HCN là {self.rong}")
       

        
    def tinhs(self):
        dtich = self.dai*self.rong
        return dtich
    def tinhchuvi(self):
        chuvi = (self.dai+self.rong)*2
        return chuvi  
      
    

dai = int(input(" nhập vào chiều dài:"))
rong = int(input(" nhập vào chiều rộng:"))
hcn = HCN(dai,rong)
print(" diện tích HCN là")
print(hcn.tinhs())
print(" chu vi hình chữ nhật là")
print(hcn.tinhchuvi())
print(" thong tin về chiểu dài và rộng sau khi nhập là ")
hcn.hienthitthcn()