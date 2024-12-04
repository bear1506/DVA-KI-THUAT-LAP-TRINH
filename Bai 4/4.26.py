print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def tinh_so_du(transactions):
  balance = 0
  for transaction in transactions.split():
    operation, amount = transaction[0], int(transaction[1:])
    if operation == 'D':
      balance += amount
    elif operation == 'W':
      balance -= amount
  return balance
if __name__ == "__main__":
  transactions = input("Nhập nhật ký giao dịch: ")
  balance = tinh_so_du(transactions)
  print("Số dư cuối cùng:", balance)
