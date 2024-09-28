n = int(input(" nhap so luong sinh vien:"))
# nhap va luu tru vao file nguyenvu.txt
for i in range(n):
    print(" nhap sinh thu ",  i+1)

    with open("nguyenvu.txt", "w") as file:
        ma = input(" nhap ma sinh vien:") + "\n"
        ten = input(" nhap ten sinh viem:") + "\n"
        lop = input(" nhap lop cua sinh vien:") + "\n"
        que = input(" nhap que quan sinh vien :") + "\n"
        file.writelines([ma,ten,lop,que])

# doc filr nguyenvu.txt
with open("nguyenvu.txt") as file:
    for sv in file.readlines():
        print(sv)
                


