import sqlite3 as sp
conn = sp.connect('product.db')
cursor = conn.cursor()  # Tạo đối tượng cursor để thực thi các lệnh SQL
# tạo bảng
cursor.execute('''
CREATE TABLE IF NOT EXISTS product(
               ID INTEGER PRIMARY KEY  AUTOINCREMENT,   
               NAME TEXT NOT NULL,
               PRICE REAL NOT NULL,
               AMOUNT INTERGER NOT NULL
               )
''') #Lệnh SQL để tạo bảng product chỉ khi bảng này chưa tồn tại
conn.commit() # lưu thay dổi vào csdl
conn.close() # đóng kết  nối


def menu():
    print('-----QUẢN LÝ SẢN PHẨM----- ')
    print(' 1.HIỂN THỊ DANH SÁCH SẢN PHẨM')
    print('2.THÊM SẢN PHẨM MỚI')
    print('3.TÌM KIẾM SẢN PHẨM THEO TÊN')
    print('4.CẬP NHẬP THÔNG TIN SẢN PHẨM')
    print('5.XÓA SẢN PHẨM')
    print('6.THOÁT')

def hienthi():
    conn = sp.connect('product.db') # kết nối to csdl
    cursor = conn.cursor() # tạo đối tượng thực thi câu lệnh trên python
    cursor.execute('SELECT * FROM product ') # truy vấn toán bộ các cột và hàng
    products = cursor.fetchall() # LẤY TẤT CAE KQUA DÃ TRUY VÂN
    for product in products:
        print(product)
 
    conn.close()


def them_san_pham():
    name = input('NHẬP TÊN SẢN PHẨM')
    price = float(input('NHẬP GIÁ SẢN PHẨM'))
    amount = int(input('NHẬP AMOUNT SẢN PHẨM'))
    conn = sp.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO product (NAME , PRICE , AMOUNT) VALUES (?,?,?)',(name,price,amount))
    conn.commit()
    conn.close()

def tim_san_pham():
    name = input(' NHẬP SẢN PHẨM THEO TÊN MUỐN TÌM')
    conn = sp.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('SELECT*FROM product WHERE NAME LIKE ?',('%'+name+'%',))
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.commit()
    conn.close()

def cap_nhap_sp():
    id = int(input(' NHẬP ID ĐỂ CẬP NHẬP GIÁ VÀ SỐ LƯỢNG'))
    price = float(input('NHẬP GIÁ CẦN ĐỔI'))
    amount = int(input(' NHẬP AMOUNT CẦN ĐỔI'))
    conn = sp.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE product SET PRICE = ? , AMOUNT = ? WHERE ID = ? ',(price,amount,id))
    conn.commit()
    conn.close()

def xoa_sp():
    id = int(input('XÓA SẢ PHẨM TRÊN ID'))
    conn = sp.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM product  Where ID = ?',(id,))
    conn.commit()
    conn.close()
    print("Xóa sản phẩm thành công!")


while True:
    menu()
    lchon = int(input('NHẬP LỰA CHỌN CỦA BẠN '))
    if lchon == 1:
        hienthi()
    elif lchon == 2:
        them_san_pham()
    elif lchon == 3:
        tim_san_pham()
    elif lchon == 4:
        cap_nhap_sp()
    elif lchon ==5:
        xoa_sp()
    elif lchon ==6:
        print('ĐÃ THOÁT')
        break
    else:
        print('LỰA CHỌN KHÔNG HỢP LỆ')




    
        








  



