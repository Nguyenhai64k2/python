print ("Sinh vien : Nguyen Dinh Hai ")
print ("MSSV 23575202161028")
print ("####################")
input_string = input("Nhập dãy các từ (cách nhau bằng khoảng trắng): ")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất có độ dài", max_length, "là:", ', '.join(longest_words))
