print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class ATM:
    def __init__(self):
        self.balance = 1000  # Số dư ban đầu
    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ!")
        else:
            self.balance -= amount
            print("Rút tiền thành công. Số dư còn lại:", self.balance)
    def deposit(self, amount):
            self.balance += amount
            print("Gửi tiền thành công. Số dư hiện tại:", self.balance)
    def check_balance(self):
        print("Số dư hiện tại:", self.balance)
# Tạo một đối tượng ATM
atm = ATM()
while True:
    print("\nChọn chức năng:")
    print("1. Rút tiền")
    print("2. Gửi tiền")
    print("3. Kiểm tra số dư")
    print("4. Thoát")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == '1':
        amount = int(input("Nhập số tiền muốn rút: "))
        atm.withdraw(amount)
    elif choice == '2':
        amount = int(input("Nhập số tiền muốn gửi: "))
        atm.deposit(amount)
    elif choice == '3':
        atm.check_balance()
    elif choice == '4':
        break
    else:
        print("Lựa chọn không hợp lệ!")
