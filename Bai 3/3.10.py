print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
##############################
import math
def Tinh(R):
    # Kiểm tra giá trị nhập vào
    if R<= 0:
        return "Bán kính phải là số dương."
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    #Trả về kết quả
    return chu_vi, dien_tich
# Nhập bán kính từ bàn phinms
R = float(input("Nhập bán kính hình tròn: "))
# Gọi hàm và in kết quả
ket_qua= Tinh(R)
if isinstance(ket_qua, tuple):
    print("Chu vi hình tròn:",ket_qua[0])
    print("Diện tích hình tròn:",ket_qua[1])
else:
    print(ket_qua)
    
