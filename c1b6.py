print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class Circle(object):
    def __init__(self, r):
        self.radius = r
        ###############################
    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print (aCircle.area()) 
