print("SV Nguyen Dinh Hai")
print(" MSSv 235752021610028")
print("#########################")
import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi người dùng nhấn nút "Click Me" hoặc phím tắt
def show_selection(event=None):
    # Lấy giá trị được chọn từ các radio button
    selected_value = var.get()
    
    # Hiển thị thông tin tương ứng với giá trị đã chọn
    if selected_value == 1:
        messagebox.showinfo("Selection", "You selected: First")
    elif selected_value == 2:
        messagebox.showinfo("Selection", "You selected: Second")
    elif selected_value == 3:
        messagebox.showinfo("Selection", "You selected: Third")
    else:
        messagebox.showwarning("No selection", "Please select an option first.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Radio Button Selection")
root.geometry("300x200")

# Tiêu đề
title_label = tk.Label(root, text="Please select an option:", font=("Helvetica", 12))
title_label.pack(pady=10)

# Tạo một biến để lưu giá trị của các radio button
var = tk.IntVar()

# Tạo các radio button
radio1 = tk.Radiobutton(root, text="First", variable=var, value=1, font=("Helvetica", 12))
radio1.pack(pady=5)

radio2 = tk.Radiobutton(root, text="Second", variable=var, value=2, font=("Helvetica", 12))
radio2.pack(pady=5)

radio3 = tk.Radiobutton(root, text="Third", variable=var, value=3, font=("Helvetica", 12))
radio3.pack(pady=5)

# Tạo nút "Click Me" để hiển thị lựa chọn
button = tk.Button(root, text="Click Me", command=show_selection, font=("Helvetica", 12))
button.pack(pady=20)

# Gán phím tắt (Enter) cho nút "Click Me"
root.bind('<Return>', show_selection)  # Phím tắt Enter

# Chạy vòng lặp sự kiện của Tkinter
root.mainloop()

