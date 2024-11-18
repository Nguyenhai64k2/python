print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đọc toàn bộ tệp văn bản và in ra nội dung
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới tệp văn bản của bạn

try:
    # Mở file để đọc
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung của file
        content = file.read()
        
        # In nội dung của file ra màn hình
        print(content)
        
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
