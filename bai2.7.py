import json

# Dữ liệu mẫu
hssv = {
    "name": "nguyenvu",
    "tuoi": 19,
    "quequan": "haiduong"
}

# Ghi dữ liệu JSON vào tệp
with open("sample.json", 'w') as file:
    json.dump(hssv, file)

# Đọc dữ liệu từ tệp JSON
with open("sample.json", 'r') as file:
    data = json.load(file)
    print(data)
