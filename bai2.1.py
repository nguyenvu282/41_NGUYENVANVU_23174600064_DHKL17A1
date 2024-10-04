import xml.etree.ElementTree as ET

# Tạo node gốc cho công ty
company = ET.Element("company")

# Thêm thông tin giám đốc
director = ET.SubElement(company, "director")
director.text = "Nguyen Van Vu"

# Thêm địa chỉ
address = ET.SubElement(company, "address")
address.text = " 1194 DUONG LANG "
# Thêm số điện thoại
phone = ET.SubElement(company, "phone")
phone.text = "045623465"

# Thêm mã số thuế
tax_code = ET.SubElement(company, "tax_code")
tax_code.text = "3485723948"

# Chuyển đổi cây XML thành chuỗi và ghi vào tệp
tree = ET.ElementTree(company)
with open("company_info.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

print("Đã lưu thông tin công ty vào file XML.")
