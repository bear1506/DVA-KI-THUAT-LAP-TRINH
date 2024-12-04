print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
#main.py
from bubble_sort import bubblesort
n=int (input("Nhap so luong phan tu cua ds:"))
nlist=[]
for _ in range(n):
    element=int(input("Nhap phan tu:"))
    nlist.append(element)
#sap xep ds
sorted_list=bubblesort(nlist)
#in kq
print("Danh sach sau khi sap xep:",sorted_list)
