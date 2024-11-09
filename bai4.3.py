import numpy as np
import pandas as pd
ser1 = pd.Series(list('gdfyfdhaghdsfgffssfhhgjdfg'))
ser2 = pd.Series(np.arange(26))
vu = pd.DataFrame({'so':ser1,'chu':ser2})
print(vu)