import json

# Đọc dữ liệu từ file JSON
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Thống kê nhân viên theo đơn vị (cách thủ công)
def employee_statistics(data):
    company_name = data.get('company_name')
    address = data.get('address')
    employees = data.get('employees')
    total_employees = len(employees)
    
    # Tạo từ điển để lưu số lượng nhân viên theo từng đơn vị
    department_stats = {}
    
    # Duyệt qua danh sách nhân viên và cập nhật số lượng theo từng đơn vị
    for employee in employees:
        department = employee['department']
        if department in department_stats:
            department_stats[department] += 1
        else:
            department_stats[department] = 1
    
    # In thông tin công ty, địa chỉ và tổng số nhân viên
    print(f"Tên công ty: {company_name}")
    print(f"Địa chỉ: {address}")
    print(f"Tổng số nhân viên: {total_employees}\n")
    
    # In thống kê nhân viên theo đơn vị
    print("Thống kê nhân viên theo đơn vị:")
    for department, count in department_stats.items():
        percentage = (count / total_employees) * 100
        print(f"- Tên đơn vị: {department}, Số nhân viên: {count}, Tỷ lệ: {percentage:.2f}%")

# Chạy chương trình
def main():
    data = read_json_file('company.json')  # Đọc file JSON
    employee_statistics(data)  # Thống kê nhân viên

if __name__ == "__main__":
    main()
