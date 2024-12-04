print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
###############################
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        """Tính diện tích hình tròn"""
        area=math.pi * self.radius**2
        return area
    def calculate_circumference(self):
        """Tính chu vi hình tròn"""
        circumference=2 * math.pi * self.radius
        return circumference
# Tạo một đối tượng hình tròn với bán kính 3
circle = Circle(3)
#Tính d.tich và chu vi
area=circle.calculate_area()
circumference=circle.calculate_circumference()
# Tính và in ra diện tích
print("Diện tích hình tròn:", area)
# Tính và in ra chu vi
print("Chu vi hình tròn:",circumference)
