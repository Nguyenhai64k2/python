print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def count_letters_and_digits(input_str):
    # Khởi tạo các biến đếm
    letter_count = 0
    digit_count = 0
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in input_str:
        if char.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái không
            letter_count += 1
        elif char.isdigit():  # Kiểm tra xem ký tự có phải là chữ số không
            digit_count += 1
    
    # In kết quả
    print(f"Số chữ cái là: {letter_count}")
    print(f"Số chữ số là: {digit_count}")

# Nhập vào câu
input_str = input("Nhập vào một câu: ")

# Gọi hàm để đếm chữ cái và chữ số
count_letters_and_digits(input_str)
