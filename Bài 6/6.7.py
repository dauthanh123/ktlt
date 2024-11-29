print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):       
        return 2 * math.pi * self.radius
circle = Circle(5)
print(f"Diện tích của hình tròn có bán kính 5 là: {circle.area()}") 
print(f"Chu vi của hình tròn có bán kính 5 là: {circle.circumference()}")  
