print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def benefit(t, n, k):
  if t <= 0 or n <= 0 or n <= k:
      print("Giá trị đầu vào không hợp lệ,vui lòng nhập lại")
      return
  for thang in range(k):
        n +=(t/100)*n
  return n    
# Nhập dữ liệu từ người dùng
t = float(input("Nhập lãi suất hàng tháng (%): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))
# Gọi hàm và in kết quả
result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
