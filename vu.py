class svien_nuocngoai():
    def __init__(self,hoten,masv,quequan):
        self.hoten = hoten
        self.masv = masv
        self.quequan = quequan
    def chao(self):
        print("hello")    


class svien_VIETNAM():
    def __init__(self,hoten,masv,quequan):
        self.hoten = hoten
        self.masv = masv
        self.quequan = quequan
    def chao(self):
        print("xin chao")
def hi(svien_VIETNAM):
    svien_VIETNAM.chao()           


sv1 = svien_nuocngoai("jane",45673,"japan")
sv2 = svien_VIETNAM("vu",384984,"hai duong")
hi(sv2)