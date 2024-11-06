print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def count_upper_lower(input_str):
    # Khởi tạo các biến đếm chữ hoa và chữ thường
    upper_count = 0
    lower_count = 0
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in input_str:
        if char.isupper():  # Kiểm tra xem ký tự có phải là chữ hoa không
            upper_count += 1
        elif char.islower():  # Kiểm tra xem ký tự có phải là chữ thường không
            lower_count += 1
    
    # In kết quả
    print(f"Chữ hoa: {upper_count}")
    print(f"Chữ thường: {lower_count}")

# Nhập vào câu
input_str = input("Nhập vào một câu: ")

# Gọi hàm để đếm chữ hoa và chữ thường
count_upper_lower(input_str)
