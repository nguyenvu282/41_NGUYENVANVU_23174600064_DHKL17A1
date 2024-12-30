import threading
import time

# Biến toàn cục
counter = 0
lock = threading.Lock()  # Lock để đồng bộ hóa

class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(4):
            time.sleep(2)
            # Sử dụng lock để đồng bộ
            with lock:
                counter += 1
                print(f"Counter đã tăng lên: {counter}")

def main():
    # Tạo danh sách các thread
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]

    # Bắt đầu các thread
    for task in tasks:
        task.start()

    # Đợi các thread hoàn thành
    for task in tasks:
        task.join()

if __name__ == "__main__":
    main()





            