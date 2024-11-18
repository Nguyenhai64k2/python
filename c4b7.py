print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đọc n dòng đầu tiên của tệp văn bản
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới tệp của bạn
n = 5  # Số dòng bạn muốn đọc (thay đổi giá trị n nếu cần)

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc n dòng đầu tiên
        for i in range(n):
            line = file.readline()
            if line == '':  # Nếu không còn dòng nào để đọc
                break
            print(line.strip())  # In ra từng dòng (strip() để loại bỏ khoảng trắng thừa)
        
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
