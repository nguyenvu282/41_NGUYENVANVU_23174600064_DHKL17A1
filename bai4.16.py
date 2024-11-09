import pandas as pd
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
diff_1 = ser.diff()
diff_2 = diff_1.diff()

print( diff_1)
print( diff_2)