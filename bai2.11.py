import json
import datetime

# Quản lý giao dịch: danh sách giao dịch, mỗi giao dịch có các thông tin cơ bản
transactions = []

# Hàm ghi giao dịch mới
def add_transaction():
    type_of_transaction = input("Loại giao dịch (tiền/vàng): ")
    amount = input("Số tiền/lượng vàng: ")
    person = input("Tên người giao dịch: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Lấy thời gian giao dịch
    
    transaction = {
        "type": type_of_transaction,
        "amount": amount,
        "person": person,
        "date": date
    }
    
    transactions.append(transaction)  # Thêm giao dịch vào danh sách

# Hàm ghi dữ liệu vào file JSON
def save_to_json_file(transactions):
    # Lấy thời gian hiện tại theo định dạng nam-thang-ngay-gio-phut-giay
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{current_time}.json"  # Tạo tên file
    
    # Ghi dữ liệu vào file JSON
    with open(file_name, 'w') as json_file:
        json.dump(transactions, json_file, indent=4)
    
    print(f"Dữ liệu đã được lưu vào tập tin {file_name}")

# Hàm thực hiện giao dịch
def main():
    while True:
        add_transaction()  # Nhập giao dịch mới
        
        continue_choice = input("Bạn có muốn thực hiện thêm giao dịch không? (có/không): ").lower()
        if continue_choice == 'không':
            break
    
    # Hỏi người dùng có muốn ghi vào file hay không
    save_choice = input("Bạn có muốn lưu các giao dịch vào file không? (1: Có / 0: Không): ")
    
    if save_choice == '1':
        save_to_json_file(transactions)  # Ghi dữ liệu vào file JSON
    else:
        print("Không ghi dữ liệu vào file.")

if __name__ == "__main__":
    main()

