import json
class jsonreader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None
    def readjson(self):
        with open(self.file_path,'r') as file:
            self.data = json.load(file)
    def display(self):
        if self.data:
            for i in self.data:
                print(f"tên:i{i['name']},tuổi:{i['age']},đchỉ:{i['address']}")
path = 'D:\\17A1KHDL\\LAB1\\DATA\\users.json'
vu = jsonreader(path)
vu.readjson()
vu.display()   
# Hàm __init__:
# Nhận tham số file_path, là đường dẫn đến file JSON cần đọc.
# Khởi tạo biến self.data để lưu dữ liệu sau khi file JSON được đọc.



# with open(self.file_path, 'r'):

# Mở file JSON từ đường dẫn được cung cấp.
# Sử dụng with để tự động đóng file sau khi đọc.
# json.load(file):

# Đọc và chuyển nội dung JSON thành danh sách Python (list) hoặc từ điển (dict).
# Trong trường hợp file JSON mẫu bạn cung cấp, nó sẽ chuyển thành một danh sách các từ điển.


# if self.data:

# Kiểm tra biến self.data có chứa dữ liệu không.
# Nếu chưa đọc file JSON, chương trình không làm gì cả.
# for user in self.data:

# Duyệt qua từng phần tử (mỗi phần tử là một từ điển chứa thông tin người dùng).
# user['name'], user['age'], user['address']:

# Truy cập giá trị của các key name, age, address trong mỗi từ điển và in ra.
