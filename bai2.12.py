import requests

# URL API chứa dữ liệu các bài post
API_URL = "https://jsonplaceholder.typicode.com/posts"

# Hàm đọc dữ liệu từ API
def get_posts_from_api():
    # Gửi yêu cầu GET tới API
    response = requests.get(API_URL)
    
    # Kiểm tra nếu kết nối thành công
    if response.status_code == 200:
        return response.json()  # Trả về dữ liệu JSON dạng list
    else:
        print("Không thể kết nối đến API.")
        return None

# Hàm hiển thị các bài post
def display_posts(posts):
    # Hiển thị tổng số bài post
    print(f"Tổng số bài post: {len(posts)}")
    
    # Hiển thị thông tin chi tiết từng bài post
    for post in posts:
        print("\n-----------------------------------")
        print(f"userID: {post['userId']}")
        print(f"id: {post['id']}")
        print(f"title: {post['title']}")
        print(f"body: {post['body']}")
        print("-----------------------------------\n")

# Hàm chính
def main():
    # Lấy danh sách các bài post từ API
    posts = get_posts_from_api()
    
    # Nếu dữ liệu lấy về thành công, hiển thị thông tin
    if posts:
        display_posts(posts)

if __name__ == "__main__":
    main()
