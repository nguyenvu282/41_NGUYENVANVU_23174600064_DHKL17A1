# khai bao class
class chim:
    def fight(self): # dinh nghia phuong thuc
        print("many bird can fly")

# khai bao lop chim se ke thua thu lop chim
class sparrow(chim):
    def fight(self):# ghi de thuong thic fight cua lop bird
        print(" chim se co the bay")

# khai bao lop da dieu ke thua tu lop chim
class dadieu:
    def fight(self):
        print(" da dieu ko bay duoc")
#__________________end_________________
oj1 = chim()
oj2=sparrow()
oj3=dadieu()
oj1.fight()        

        



