class Stack:
    def __init__(self, size):
        # Khởi tạo ngăn xếp với kích thước cho trước
        self.stack = []
        self.max_size = size

    def is_empty(self):
        # Kiểm tra xem ngăn xếp có rỗng không
        return len(self.stack) == 0

    def is_full(self):
        # Kiểm tra xem ngăn xếp đã đầy chưa
        return len(self.stack) == self.max_size

    def push(self, item):
        # Thêm một phần tử vào ngăn xếp nếu chưa đầy
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Ngăn xếp đã đầy!")

    def pop(self):
        # Lấy một phần tử từ đỉnh ngăn xếp nếu ngăn xếp không rỗng
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Ngăn xếp rỗng, không thể pop!")

    def peek(self):
        # Xem phần tử ở đỉnh ngăn xếp
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Ngăn xếp rỗng!")

    def print_stack(self):
        # In ra nội dung của ngăn xếp
        if self.is_empty():
            print("Ngăn xếp rỗng!")
        else:
            print("Nội dung ngăn xếp:", self.stack)


# Ví dụ sử dụng
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()  # In ra nội dung ngăn xếp

stack.pop()  # Lấy phần tử từ đỉnh ngăn xếp
stack.print_stack()  # In lại nội dung sau khi pop
