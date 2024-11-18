print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Mở file để đọc
file_path = 'file.txt'  # Thay 'duongdan/file.txt' bằng đường dẫn đến file của bạn

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc tất cả nội dung của file
        content = file.read()
        
        # In nội dung theo thứ tự đảo ngược
        print(content[::-1])
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
