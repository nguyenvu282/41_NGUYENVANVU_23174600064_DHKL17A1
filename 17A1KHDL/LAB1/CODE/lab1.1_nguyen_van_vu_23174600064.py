import xml.etree.ElementTree as et # gọi hàm để dungf tvien xml
class xmlreader:
    def __init__(self,file_path): # khởi tạo constructor của lớp
        self.file_path = file_path # thuộc tính truyền đường dẫn
        self.data = None # thuộc tính để lưu dữ liệu
    def readxml(self): # phương thức đọc file xml
        tree = et.parse(self.file_path) #
        self.data = tree.getroot() # Lấy nút gốc (root element) của cây XML (products)
    def display_data(self):
        if self.data:
            for product in self.data.findall('product'):     
                name = product.find('name').text
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(name,'\n',price,'\n',quantity)
path = 'D:\\17A1KHDL\\LAB1\\DATA\\products.xml'
reader = xmlreader(path)
reader.readxml()
reader.display_data()




#1. Đọc và phân tích cú pháp file XML
#et.parse(file_path):
# Phân tích cú pháp file XML từ đường dẫn file_path (products.xml).
# Kết quả là một cây (tree) XML chứa tất cả các node và thuộc tính từ file.
# 2. Lấy nút gốc (<products>)
# tree.getroot():
# Trả về phần tử gốc của cây XML, ở đây là <products>.
# 3. Tìm tất cả các node con <product>
# self.data.findall('product'):
# Tìm tất cả các node <product> là con trực tiếp của <products>.
# Trả về một danh sách các node <product>.
# 4. Truy cập từng thẻ con của <product>
# product.find('name').text:
# Với mỗi <product>, tìm thẻ <name> bên trong nó.
# Lấy nội dung văn bản bên trong thẻ <name> (ví dụ: duong).
# 5. Hiển thị dữ liệu
# Lặp qua từng <product> trong danh sách, lấy nội dung từ các thẻ <name>, <price>, <quantity>, <units>, và in chúng ra.

