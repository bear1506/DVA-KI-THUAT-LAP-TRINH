print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def tim_so_dac_biet(n):
   for i in range(1,n):
       tong_uoc=0
       for j in range(1,i+1):
           if i%j==0:
              tong_uoc+=j
       if tong_uoc>i:
           print(i)
n=int(input("Nhao so nguyen duong n:"))
tim_so_dac_biet(n)
    
