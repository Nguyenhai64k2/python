print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
# Đoạn văn bản bạn muốn nối vào tệp
text_to_append = """
Đây là một đoạn văn bản mới.
Chúng tôi đang thử nghiệm nối văn bản vào tệp.
"""

# Đường dẫn tới tệp
file_path = 'file.txt'  # Thay 'file.txt' bằng đường dẫn tới tệp của bạn

try:
    # Mở tệp ở chế độ append ('a') để nối văn bản vào cuối tệp
    with open(file_path, 'a', encoding='utf-8') as file:
        # Nối văn bản vào tệp
        file.write(text_to_append)
        print(f"Văn bản đã được nối vào tệp {file_path}")
    
    # Mở lại tệp ở chế độ đọc ('r') để hiển thị nội dung
    with open(file_path, 'r', encoding='utf-8') as file:
        print("\nNội dung tệp sau khi nối:")
        print(file.read())  # Đọc và in toàn bộ nội dung tệp

except FileNotFoundError:
    print(f"Không tìm thấy tệp: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
