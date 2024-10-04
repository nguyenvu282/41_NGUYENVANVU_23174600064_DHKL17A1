import xml.dom.minidom as minidom

# Tải và phân tích tài liệu XML
doc = minidom.parse("sample.xml")

# Lấy danh sách các phần tử <name>
names = doc.getElementsByTagName("name")

# In ra tên của từng phần tử <name>
for name in names:
    print(name.firstChild.data)
