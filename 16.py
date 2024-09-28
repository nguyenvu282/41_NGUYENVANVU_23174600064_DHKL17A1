class dogs:
    dogcount = 0 # khởi tạo đối tượng
    def __init__(self,name,size,age,coler):
        self.name = name # thuoc tính đối tượng
        self.size = size
        self.age = age
        self.coler = coler
    def go(self):
        print(" dog đang đi" ) # hành vi (hoạt động)
    def stay(self , place):
        print(" dog đang where" ,place)
    def lie(self,place):
        print(" cún đang nằm {}".format(place))
    def bark(self):
        print(" whoo")
    def eat(self,food):
        print(" cún đang ăn ".format(food))


bul = dogs("bull",'bigsize',19,'yellow'
           )            
bul.stay(" garden")
bul.bark()
