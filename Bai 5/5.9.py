print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
#main.py
from binary_search import binary_search
#nhap sluong p.tu
n= int(input("Nhap so luong phan tu cua danh sanh:"))
num_list=[]
#nhap p.tu ds
for _ in range (n):
       element=int(input("nhap phan tu:"))
       num_list.append(element)
#sap xep ds
num_list.sort()
#nhap g.tri can tim
value=int(input("Nhap gia tri can tim:"))
#goi ham tim kiem
found= binary_search(num_list,value)
#in ket qua
if found:
 print(f"gia tri {value} duoc tim thay trong ds.")
else:
 print(f"gia tri {value} khong duoc tim thay trong ds.")   
                   
 
