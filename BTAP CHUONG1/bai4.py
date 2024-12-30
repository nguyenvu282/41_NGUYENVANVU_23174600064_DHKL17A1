# Xay dung lop
class Stack:

    # Ham khoi tao
    def __init__(self):
        self.s = []

    # Ham bo sung
    def push(self, x):
        self.s.append(x)

    # Ham loai bo
    def pop(self):
        if len(self.s) == 0:
            return "stack is empty"
        return self.s.pop()

    # Ham kiem tra Ngan xep rong
    def is_empty(self):
        return len(self.s) == 0


    # Ham kiem tra Ngan xep day
S = Stack()
S.push(int(input('Nhap phan tu : ')))
S.pop()
S.is_empty()