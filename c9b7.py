print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import shutil

# Đường dẫn tới tệp nguồn và tệp đích
source_file = 'source.txt'  # Thay 'source.txt' bằng đường dẫn tới tệp nguồn của bạn
destination_file = 'destination.txt'  # Thay 'destination.txt' bằng đường dẫn tới tệp đích của bạn

try:
    # Sao chép nội dung tệp nguồn vào tệp đích
    shutil.copy(source_file, destination_file)
    print(f"Tệp {source_file} đã được sao chép sang {destination_file}")
except FileNotFoundError:
    print(f"Tệp nguồn không tồn tại: {source_file}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
