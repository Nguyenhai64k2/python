print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đọc n dòng cuối cùng của tệp văn bản
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới tệp của bạn
n = 5  # Số dòng bạn muốn đọc (thay đổi giá trị n nếu cần)

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung tệp và lưu thành một danh sách các dòng
        lines = file.readlines()
        
        # Lấy n dòng cuối cùng
        last_n_lines = lines[-n:]  # Dùng slicing để lấy n dòng cuối
        
        # In các dòng cuối cùng
        print(f"\n{n} dòng cuối cùng của tệp:")
        for line in last_n_lines:
            print(line.strip())  # Dùng strip() để loại bỏ ký tự xuống dòng
        
except FileNotFoundError:
    print(f"Không tìm thấy tệp: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
