import pandas as pd
import numpy as np

# Tạo dữ liệu ngẫu nhiên
hmm = pd.Series(np.random.randint(1, 10, 35))

# Định hình lại ser thành DataFrame với 7 hàng và 5 cột
df = pd.DataFrame(hmm.values.reshape(7, 5))

print(df)
