print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def filter_odd_numbers(input_str):
    # Chuyển chuỗi nhập vào thành danh sách các số nguyên
    numbers = list(map(int, input_str.split(',')))
    
    # Lọc các số lẻ
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # In kết quả
    return ','.join(map(str, odd_numbers))

# Nhập chuỗi các số từ người dùng
input_str = input("Nhập các số (cách nhau bởi dấu phẩy): ")

# Lọc các số lẻ và in ra kết quả
result = filter_odd_numbers(input_str)
print(result)
