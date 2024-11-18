print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Danh sách nội dung cần ghi vào tệp
data = [
    "Dòng 1: Hello, world!",
    "Dòng 2: Python là một ngôn ngữ lập trình tuyệt vời.",
    "Dòng 3: Học Python rất thú vị."
]

# Đường dẫn tới tệp
file_path = 'output.txt'  # Thay 'output.txt' bằng đường dẫn tới tệp của bạn

try:
    # Mở tệp ở chế độ ghi ('w'). Nếu tệp đã tồn tại, nó sẽ bị ghi đè
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line + '\n')  # Ghi từng dòng và thêm ký tự xuống dòng

    print(f"Nội dung đã được ghi vào tệp {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
