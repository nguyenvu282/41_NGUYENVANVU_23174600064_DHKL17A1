import pandas as pd
import numpy as np
#a
data = pd.read_csv('D:\\17A1KHDL\\LAB2\DATA\\diem_hoc_phan.csv')
diem_list = data[['HP 1','HP 2','HP 3']].values.tolist() # trả về 1 mảng numpy sau đó truyển thành list
diem_numpyy = np.array(diem_list)
#print('sau khi thêm điểm vào list \n',diem_numpyy)
#b 
def qdoi_diem(diem):
    if 8.5<=diem<=10:
        return 'A'
    elif 8.0<=diem<=8.4:
        return 'B+'
    elif 7.0<=diem<8:
        return 'B'
    elif 6.5<=diem<7.0:
        return 'C+'
    elif 5.5<=diem<6.0:
        return 'C'
    elif 5.0<=diem<5.5:
        return 'D+'
    elif 4.0<=diem<5.0:
        return 'D'
    else:
        return 'F'
    
diem_chu = []
for i in diem_numpyy:
    diem_moi = []
    for j in i:
        diem_moi.append(qdoi_diem(j))
    diem_chu.append(diem_moi)
#print('sau đổi từ số sang chữ\n',diem_chu)
diem_chữ = [[qdoi_diem(j) for j in i] for i in diem_numpyy]
#print(diem_chữ)
#c
diem_hp1 = diem_numpyy[:,0]
diem_hp2 = diem_numpyy[:,1]
diem_hp3 = diem_numpyy[:,2]
# print('điểm hp1 sau khi tác\n',diem_hp1)
# print('điểm hp2 sau khi tác\n',diem_hp2)
# print('điểm hp3 sau khi tác\n',diem_hp3)
# d
def ptich_hp(hp):
    tong = np.sum(hp)
    hp_tb = np.mean(hp)
    dlc = np.std(hp)
    print('tổng điểm là\n',tong)
    print('điểm số tb là\n',hp_tb)
    print('độ lệch chuẩn của điểm hp là\n',dlc)
# vu = ptich_hp(diem_hp1)
# vux = ptich_hp(diem_hp2)
# xu = ptich_hp(diem_hp3)
#print(vu)    
# e

diem_tong_hop = {}
for i in diem_chữ:
    for j in i:
        if j in diem_tong_hop:
            diem_tong_hop[j]+=1
        else:
            diem_tong_hop[j] =1
print(diem_tong_hop)            
print('số lượng svien đạt các điểm là')            
for diem,soluong in diem_tong_hop.items():
     print(f'điểm{diem} : {soluong}')            
        

