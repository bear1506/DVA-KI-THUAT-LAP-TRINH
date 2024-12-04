print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
#main.py
from mymodule import sort_list, find_maximum, find_minimum
def main():
    n=int(input("Nhap so luong phan tu cua danh sach:"))
    input_list=[]
    for i in range(n):
        num=float(input(f"Nhap phan tu thu{i+1}:"))
        input_list.append(num)
    sorted_list= sort_list(input_list)
    max_value=find_maximum(sorted_list) 
    min_value=find_minimum(sorted_list) 
    print(f"Phan tu lon nhat: {max_value}")
    print(f"Phan tu nho nhat: {min_value}")
if __name__=="__main__":
    main()
