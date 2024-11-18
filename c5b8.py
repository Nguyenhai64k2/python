print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import tkinter as tk
from tkinter import PhotoImage

# Hàm xử lý khi lựa chọn thay đổi
def on_radio_select():
    selected_value.set(f"Lựa chọn của bạn là: {selection.get()}")

# Tạo cửa sổ đồ họa
window = tk.Tk()
window.title("Radio Button với Indicator hình ảnh")
window.geometry("400x300")  # Đặt kích thước cửa sổ

# Khởi tạo biến để lưu giá trị lựa chọn
selection = tk.StringVar()

# Thêm một label để hiển thị lựa chọn
selected_value = tk.Label(window, text="Chưa chọn lựa chọn nào")
selected_value.pack(pady=20)

# Tải hình ảnh cho các lựa chọn
image1 = PhotoImage(file="icon1.png")  # Thay bằng đường dẫn đến hình ảnh của bạn
image2 = PhotoImage(file="icon2.png")  # Thay bằng đường dẫn đến hình ảnh của bạn
image3 = PhotoImage(file="icon3.png")  # Thay bằng đường dẫn đến hình ảnh của bạn

# Thêm các radio button sử dụng hình ảnh làm indicator
radio_button1 = tk.Radiobutton(window, text="Lựa chọn 1", variable=selection, value="Lựa chọn 1", image=image1, compound="left", command=on_radio_select)
radio_button1.pack(pady=10)

radio_button2 = tk.Radiobutton(window, text="Lựa chọn 2", variable=selection, value="Lựa chọn 2", image=image2, compound="left", command=on_radio_select)
radio_button2.pack(pady=10)

radio_button3 = tk.Radiobutton(window, text="Lựa chọn 3", variable=selection, value="Lựa chọn 3", image=image3, compound="left", command=on_radio_select)
radio_button3.pack(pady=10)

# Khởi động vòng lặp giao diện đồ họa
window.mainloop()
