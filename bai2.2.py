import xml.etree.ElementTree as ET

# Tạo node gốc cho danh sách sinh viên
students = ET.Element("students")

# Thông tin sinh viên 1
student_1 = ET.SubElement(students, "student")
ET.SubElement(student_1, "id").text = "23174600064"
ET.SubElement(student_1, "name").text = "Nguyen Van Vu"
ET.SubElement(student_1, "birth_year").text = "2006"
ET.SubElement(student_1, "class").text = "17A1"
ET.SubElement(student_1, "gender").text = "Nam"

# Chuyển đổi cây XML thành chuỗi và ghi vào tệp
tree = ET.ElementTree(students)
with open("students.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

print("Đã lưu danh sách sinh viên vào file XML.")
