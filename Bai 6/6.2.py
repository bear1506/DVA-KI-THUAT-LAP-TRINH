print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class Hinhchunhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def tinh_dien_tich(self):
        return self.chieudai * self.chieurong
#Vd:hình chữ nhật có c.dai 4, c.rong 3
hinh_chu_nhat = Hinhchunhat(4, 3)
#kq và in ra
print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())
