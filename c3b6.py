print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class Nguoi(object):
    def getGender(self):
        return "Unknown"  
class Nam(Nguoi):
    def getGender(self):
        return "Nam"  
class Nu(Nguoi):
    def getGender(self):
        return "Nữ" 
aNam = Nam()
aNu = Nu()
print(aNam.getGender())  
print(aNu.getGender())   
