print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class ReverseWordsOrder:
    def __init__(self, text):
        self.text = text 
    def reverse_word_order(self):
        words = self.text.split()  
        reversed_order = words[::-1]  
        return ' '.join(reversed_order)  
input_text = input("Nhập chuỗi: ")
reverse_order = ReverseWordsOrder(input_text)
result = reverse_order.reverse_word_order()

print("Chuỗi sau khi đảo ngược thứ tự các từ:", result)

