print('sinh vien:Đậu Đức Thành')
print('mssv:235752021610004')
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(2)
print("Diện tích hình tròn:", circle.area())
