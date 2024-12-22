import numpy as np
#a
# Đọc dữ liệu từ tệp efficiency.txt
with open('D:\\17A1KHDL\\LAB2\DATA\\efficiency.txt', 'r') as tep:
    hieu_suat = [float(dong.strip()) for dong in tep] # xóa dấu cách và kí tự xuống dòng

# Đọc dữ liệu từ tệp shifts.txt
with open('D:\\17A1KHDL\\LAB2\DATA\\shifts.txt', 'r') as tep:
    ca_lam_viec = [dong.strip() for dong in tep]
    
#b
np_ca_lam_viec = np.array(ca_lam_viec)
#print("Kiểu dữ liệu của np_ca_lam_viec:", np_ca_lam_viec.dtype)
#c
np_hieu_suat = np.array(hieu_suat)
print("Kiểu dữ liệu của np_hieu_suat:", np_hieu_suat.dtype)
#d
hieu_suat_morning = np_hieu_suat[np_ca_lam_viec == 'Morning']
tb_hieu_suat_morning = np.mean(hieu_suat_morning)
print("Hiệu suất trung bình của ca Morning:", tb_hieu_suat_morning)
#e 
hieu_suat_khac = np_hieu_suat[np_ca_lam_viec != 'Morning']
tb_hieu_suat_khac = np.mean(hieu_suat_khac)
print("Hiệu suất trung bình của các ca khác:", tb_hieu_suat_khac)
#g
nhan_vien = np.array(
    list(zip(np_ca_lam_viec, np_hieu_suat)),
    dtype=[('ca', 'U10'), ('hieu_suat', 'float')]
)
print(nhan_vien)
#h
nhan_vien_sap_xep = np.sort(nhan_vien, order='hieu_suat')
hieu_suat_cao_nhat = nhan_vien_sap_xep[-1]
hieu_suat_thap_nhat = nhan_vien_sap_xep[0]
print("Ca làm việc hiệu suất cao nhất:", hieu_suat_cao_nhat)
print("Ca làm việc hiệu suất thấp nhất:", hieu_suat_thap_nhat)


