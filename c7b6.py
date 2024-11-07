print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius
radius = float(input("Nhập bán kính hình tròn: "))
circle = Circle(radius)
print(f"Diện tích của hình tròn: {circle.area():.2f}")
print(f"Chu vi của hình tròn: {circle.circumference():.2f}")
