print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class StringManipulator:
    def __init__(self):
        self.user_string = ""   
    def get_String(self):
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())
string_obj = StringManipulator()
string_obj.get_String()
string_obj.print_String()
