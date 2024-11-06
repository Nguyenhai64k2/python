print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def find_even_digit_numbers(start, end):
    # Danh sách để lưu các số có tất cả chữ số chẵn
    even_digit_numbers = []
    
    # Duyệt qua tất cả các số trong khoảng từ start đến end
    for num in range(start, end + 1):
        # Chuyển số thành chuỗi để kiểm tra từng chữ số
        num_str = str(num)
        # Kiểm tra nếu tất cả các chữ số đều là số chẵn
        if all(digit in '02468' for digit in num_str):
            even_digit_numbers.append(num_str)
    
    # Trả về danh sách các số có tất cả chữ số chẵn, phân tách bằng dấu phẩy
    return ','.join(even_digit_numbers)

# Đoạn số từ 1000 đến 3000
start = 1000
end = 3000

# Tìm và in các số
result = find_even_digit_numbers(start, end)
print(result)


