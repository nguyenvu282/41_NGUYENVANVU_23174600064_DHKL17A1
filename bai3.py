class ps:
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso=mauso
    def tinhhople(self):
        while(self.mauso == 0):
            print("nhap lai mau so vs mau so khac 0 ")
        
            self.mauso = int(input(" nhap lai mau so:"))
        
    
    def hienthips(self):
        print(f"phân số  sau khi in ra man  hinh la :{self.tuso}/{self.mauso}")
    
           

tuso = int(input(" nhap tu so:"))
mauso = int(input(" nhạp mẫu số:"))

pso = ps(tuso,mauso)
pso.tinhhople()

pso.hienthips() 
        

