print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đếm số dòng trong tệp văn bản
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới tệp của bạn

try:
    # Mở tệp ở chế độ đọc
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ tệp và lưu vào danh sách
        lines = file.readlines()
        
        # Đếm số dòng
        num_lines = len(lines)
        
        print(f"Số dòng trong tệp: {num_lines}")

except FileNotFoundError:
    print(f"Không tìm thấy tệp: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
