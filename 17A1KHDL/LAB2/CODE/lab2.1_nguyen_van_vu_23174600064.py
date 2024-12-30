import numpy as np
#a
nhietdo = np.round(np.random.uniform(15.0,31.0,30),2)
nd_tb = np.mean(nhietdo)
print('dữ liệu nhiệt độ hàng ngày trong 1thangg\n',nhietdo)
print('nhiệt độ tb là\n',nd_tb)
#b 
caonhat = np.max(nhietdo)
thapnhat = np.min(nhietdo)
print("ngày có nhiệt độ cao nhất là\n",caonhat)
print('ngyaf có nhiệt độ thấp nhất là\n',thapnhat)
# Xác định vị trí của các nhiệt độ này trong mảng
vtri_nd_caonhat = np.argmax(nhietdo) +1
vtri_nd_thnhat = np.argmin(nhietdo) +1
print('ngày có nhiệt độ cao nhất là\n',vtri_nd_caonhat)
print('ngày có nhiệt độ thấp nhất tháng\n',vtri_nd_thnhat)
# # Xác định sự chênh lệch lớn nhất và ngày xảy ra sự chênh lệch đó
ngaytrc = nhietdo[1:]
ngaysau = nhietdo[:1]
chenhlech = ngaysau-ngaytrc
daymax = np.argmax(np.abs(chenhlech))+1
max_cl = chenhlech[daymax-1]
print('ngày chenh lech cao nhat\n',daymax)
print('chenh lệch  lớn nhất là\n',max_cl)
#c
print('ngày có nhiệt độ cao hơn 20 độ xê\n',np.where(nhietdo>20)[0]+1) # trả về 1 tuple(ptu duy nhất)[0] đc
#sdung để lấy mảng chỉ số
ngay_db = [4,9,14,19,24]
print('nhiệt độ của ngày 5,10,15,20,25\n',nhietdo[ngay_db])
#Tìm nhiệt độ của các ngày có nhiệt độ trên trung bình
for index,value in enumerate(nhietdo): #giúp bạn có cả chỉ số và giá trị của phần tử trong vòng lặp
    if value>nd_tb:
        print(f'ngày{index+1}:{value}'
              )
      

# Lấy nhiệt độ của các ngày chẵn/lẻ trong tháng.
ngay_chan =[]
ngay_le = []
for vtri,gtri in enumerate(nhietdo):
    if (vtri+1)%2==0:
        ngay_chan.append((f'ngày {vtri}:nhiệt độ{gtri}'))
    else:
        ngay_le.append((f'ngày{vtri}:nhiệt đô{gtri}'))
print(" nhiệt độ ngày chẵn \n",ngay_chan)
print('nhiệt độ ngyaf lẻ\n',ngay_le)        

    

