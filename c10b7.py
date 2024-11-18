print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import string

# Hàm tìm những từ dài nhất trong văn bản
def find_longest_words(text):
    # Tách văn bản thành các từ (loại bỏ dấu câu)
    words = text.split()
    
    # Loại bỏ dấu câu khỏi các từ (chẳng hạn như dấu chấm, phẩy, ...)
    words = [word.strip(string.punctuation) for word in words]
    
    # Tìm chiều dài của các từ
    max_length = max(len(word) for word in words)
    
    # Tìm những từ có chiều dài bằng max_length
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words, max_length

# Đọc văn bản từ tệp
file_path = 'example.txt'  # Thay 'example.txt' bằng đường dẫn tới tệp của bạn

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung tệp
        text = file.read()
        
        # Tìm những từ dài nhất
        longest_words, max_length = find_longest_words(text)
        
        # In kết quả
        print(f"Các từ dài nhất (dài {max_length} ký tự):")
        for word in longest_words:
            print(word)

except FileNotFoundError:
    print(f"Tệp không tồn tại: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
