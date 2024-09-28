class dog:
    def __init__(self,name,size,age,coler):
        self.name = name
        self.size=size
        self.age=age
        self.coler=coler
        # lay 1 thuoc tinh name dunng getter
    def get_name(self):
        return self.name
    def set_age(self, new_value):
        self.age=new_value

dg1 = dog("bull",'big','5','yellow')
#print(dg1.get_name())
print(dg1.set_age("9"))