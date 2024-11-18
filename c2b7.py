print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đọc file và tính số ký tự, số từ, số dòng
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới file của bạn

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Khởi tạo các biến đếm
        num_chars = 0
        num_words = 0
        num_lines = 0
        
        # Đọc từng dòng trong file
        for line in file:
            # Đếm số dòng
            num_lines += 1
            
            # Đếm số từ trong dòng
            words = line.split()  # Tách dòng thành các từ, mặc định là tách theo khoảng trắng
            num_words += len(words)
            
            # Đếm số ký tự trong dòng
            num_chars += len(line)
        
        # In kết quả
        print(f"Số ký tự: {num_chars}")
        print(f"Số từ: {num_words}")
        print(f"Số dòng: {num_lines}")

except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
