print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
# Tạo đối tượng hình tròn với bán kính 2
circle = Circle(2)
# Tính diện tích và in ra kết quả
print("Diện tích hình tròn:", circle.area())
