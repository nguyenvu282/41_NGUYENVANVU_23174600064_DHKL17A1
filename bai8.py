class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    # Phương thức kiểm tra xem một năm có phải là năm nhuận không
    def is_leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    # Phương thức tính số ngày trong tháng
    def days_in_month(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        else:
            return 0

    # Phương thức hiển thị ngày
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    # Phương thức tính ngày tiếp theo
    def next_day(self):
        self.day += 1
        if self.day > self.days_in_month(self.month, self.year):
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Sử dụng lớp Date
date = Date(28, 2, 2023)  
date.display()  

date.next_day()  
date.display()  
