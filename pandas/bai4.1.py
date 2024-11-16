import pandas as pd
import numpy as np
# 1
mlist = list('asdgyewfwgrgwrdbfshgff')
kk = pd.Series(mlist)
#print(kk)
#2
myarr = np.arange(26)
hmm = pd.Series(myarr)
#print(hmm)
mydicyt = dict(zip(mlist,myarr))
vu = pd.Series(mydicyt)
print(vu)