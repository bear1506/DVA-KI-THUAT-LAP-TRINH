print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
from Sequential_search import Sequential_search
n=int (input("Nhap so luong phan tu cua danh sach:"))
dlist=[]
for _ in range(n):
    element=int(input("Nhap phan tu:"))
    dlist.append(element)
item=int(input("Nhap phan tu can tim:"))
result=Sequential_search(dlist,item)
#in kqua
if result[0]:
   print(f"Phan tu(item)duoc tim thay tai muc{result[1]}.")
else:
    print(f"phan tu{item}khong duoc tim thay.")

    
