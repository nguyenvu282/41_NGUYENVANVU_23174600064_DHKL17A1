class Stack:
    # Hàm khởi tạo với kích thước ngăn xếp
    def __init__(self, size):
        self.stack = []  # Ngăn xếp khởi tạo rỗng
        self.size = size  # Kích thước tối đa của ngăn xếp
    
    # Hàm kiểm tra ngăn xếp có trống không
    def isEmpty(self):
        return len(self.stack) == 0
    
    # Hàm kiểm tra ngăn xếp có đầy không
    def isFull(self):
        return len(self.stack) == self.size
    
    # Hàm thêm phần tử vào ngăn xếp
    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.stack.append(item)  # Thêm phần tử vào ngăn xếp
            print(f"Đã thêm {item} vào ngăn xếp.")
    
    # Hàm lấy phần tử từ đỉnh ngăn xếp ra
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống! Không thể lấy phần tử.")
            return None
        else:
            item = self.stack.pop()  # Lấy phần tử ra khỏi ngăn xếp
            print(f"Đã lấy {item} ra khỏi ngăn xếp.")
            return item
    
    # Hàm hiển thị ngăn xếp
    def display(self):
        if self.isEmpty():
            print("Ngăn xếp trống!")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)


# Sử dụng lớp Stack
size = int(input("Nhập kích thước ngăn xếp: "))
ngan_xep = Stack(size)

# Các thao tác trên ngăn xếp
ngan_xep.push(10)
ngan_xep.push(20)
ngan_xep.push(30)

ngan_xep.display()  

ngan_xep.pop()  

ngan_xep.display()  
ngan_xep.push(40)
ngan_xep.display()
