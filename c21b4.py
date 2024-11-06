print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def check_divisible_by_5(binary_numbers):
    # Lưu các số nhị phân chia hết cho 5 vào danh sách
    divisible_by_5 = []
    
    # Duyệt qua từng số nhị phân
    for binary in binary_numbers:
        # Chuyển từ nhị phân sang thập phân
        decimal = int(binary, 2)
        # Kiểm tra nếu chia hết cho 5
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    
    # Trả về danh sách các số nhị phân chia hết cho 5, phân tách bởi dấu phẩy
    return ','.join(divisible_by_5)

# Nhập vào chuỗi các số nhị phân 4 chữ số phân tách bởi dấu phẩy
input_str = input("Nhập chuỗi các số nhị phân 4 chữ số phân tách bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_str.split(',')

# Gọi hàm kiểm tra và in kết quả
result = check_divisible_by_5(binary_numbers)
print("Các số nhị phân chia hết cho 5 là:", result)
