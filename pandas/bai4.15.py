import pandas as pd
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
ser = ser.str.capitalize()

print(ser)