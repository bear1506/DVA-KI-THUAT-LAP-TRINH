print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def So_fibonacci(n):
    fib_list=[]
    a,b=0,1
    while a < n:
        fib_list.append(a)
        a,b=b, a + b
    return fib_list
n= int(input("Nhap so nguyen duong n:"))
fib_list=So_fibonacci(n)
print("Danh sach cac so fibonacci nho hon:",n,":")
print(fib_list)
