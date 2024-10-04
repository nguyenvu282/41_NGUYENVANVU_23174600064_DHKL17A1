import xml.dom.minidom as minidom

# Tải file XML
doc = minidom.parse("sample.xml")

# Lấy tên công ty
company_name = doc.getElementsByTagName("name")[0].firstChild.data
print("Tên công ty:", company_name)

# Lấy danh sách nhân viên
staff_list = doc.getElementsByTagName("staff")

# Duyệt qua từng nhân viên và in thông tin
for staff in staff_list:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data.strip()
    staff_salary = staff.getElementsByTagName("salary")[0].firstChild.data.strip()
    
    print(f"ID: {staff_id}, Tên: {staff_name}, Lương: {staff_salary}")
