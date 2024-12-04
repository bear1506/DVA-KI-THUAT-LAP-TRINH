print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class Nguoi:
    def get_gender(self):
        return "Không xác định"
class Nam(Nguoi):
    def get_gender(self):
        return "Nam"
class Nu(Nguoi):
    def get_gender(self):
        return "Nữ"
# Tạo đối tượng
nam1 = Nam()
nu1 = Nu()
# Gọi method get_gender()
print(nam1.get_gender())
print(nu1.get_gender()) 
