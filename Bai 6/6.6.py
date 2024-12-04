print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class Chuoi:
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("Nhập vào một chuỗi: ")
    def print_String(self):
        print(self.str1.upper())
#Tạo một đối tượng của class Chuoi
obj = Chuoi()
#Gọi phương thức get_String để nhập chuỗi
obj.get_String()
#Gọi phương thức print_String để in chuỗi ra màn hình
obj.print_String()        


