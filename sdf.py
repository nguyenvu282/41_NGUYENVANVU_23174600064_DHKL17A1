# minh hoa cac ham có sẵn trong python
class dogs:
    dogcount = 0 # khởi tạo đối tượng
    def __init__(self,name,size,age,coler):
        self.name = name # thuoc tính đối tượng
        self.size = size
        self.age = age
        self.coler = coler

# tạp đối tượng lớp dogs
husky = dogs(" bull", 'big',"5","yellow")
print(getattr(husky,'name'))    # lấy 1 thuộc tính cụ thẻ
# gán giá trị cho age la 6
print(setattr(husky,"age", 3))
print(getattr(husky,"age"))
# kiem tra thuoc tinnh co hay ko
print(hasattr(husky, " que quan"))
# sử dụng del để xóa thuộc tính 
print(delattr(husky, " age"))
# sau khi xoa in ra thu 
print(husky.age)