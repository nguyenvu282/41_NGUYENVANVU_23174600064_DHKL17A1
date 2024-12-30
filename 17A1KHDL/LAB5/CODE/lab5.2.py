import time
import threading
class simpletask():
    def run_stack(self):
        
        for i in range(1,4):
            print('chạy lần thứ ',i)
            time.sleep(1)
def main():
    tasks = [threading.Thread(target=simpletask().run_stack()) for _ in range(4)]   
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()
        