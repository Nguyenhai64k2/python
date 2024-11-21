print("SV Nguyen Dinh Hai ")
print("MSSV 2357520216100280")
print("#########################")
import tkinter as tk

# Khởi tạo cửa sổ chính
root = tk.Tk()

# Khởi tạo biến IntVar để lưu giá trị lựa chọn
v = tk.IntVar()
v.set(1)  # Khởi tạo lựa chọn ban đầu là Python

# Danh sách các ngôn ngữ lập trình với giá trị lựa chọn
languages = [
    ("Python", 1),
    ("Perl2", 2),
    ("Java3", 3),
    ("C++4", 4),
    ("C5", 5)
]

# Hàm xử lý khi người dùng chọn một ngôn ngữ
def ShowChoice():
    print(f"Bạn đã chọn ngôn ngữ có ID: {v.get()}")

# Nhãn hiển thị hướng dẫn
tk.Label(root, 
         text="""Choose your favourite  
         programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các nút radio cho các ngôn ngữ
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,  # Hiển thị tên ngôn ngữ
                   padx=20,
                   variable=v,  # Biến lưu giá trị lựa chọn
                   command=ShowChoice,  # Lệnh gọi hàm ShowChoice khi thay đổi lựa chọn
                   value=val).pack(anchor=tk.W)

# Chạy vòng lặp chính để hiển thị giao diện
root.mainloop()
