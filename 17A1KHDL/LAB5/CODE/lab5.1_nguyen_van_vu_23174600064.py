import time
class simpletask():
    def run_stack(self):
        for i in range(1,11):
            print('in dòng thứ ',i)
            time.sleep(2)
def main():
    task = simpletask()
    task.run_stack()    

if __name__ == "__main__":
    main()
      