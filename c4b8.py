print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import tkinter as tk

# Hàm xử lý sự kiện phím bấm
def on_key_press(event):
    label.config(text=f"Bạn đã nhấn phím: {event.char}")

# Tạo cửa sổ đồ họa
window = tk.Tk()
window.title("Cửa sổ đồ họa với Button và Sự kiện phím bấm")
window.geometry("400x300")  # Đặt kích thước cửa sổ

# Thêm một widget button và thay đổi màu nền (bg) và màu chữ (fg)
def on_button_click():
    label.config(text="Button đã được nhấn!")

button = tk.Button(window, text="Nhấn tôi!", command=on_button_click, bg="blue", fg="white")
button.pack(pady=20)  # Đặt button vào cửa sổ và thêm khoảng cách

# Thêm một widget label để hiển thị thông tin
label = tk.Label(window, text="Chưa nhấn phím hoặc button.")
label.pack(pady=20)

# Xử lý sự kiện phím bấm
window.bind("<KeyPress>", on_key_press)  # Liên kết sự kiện nhấn phím với phương thức on_key_press

# Khởi động vòng lặp giao diện đồ họa
window.mainloop()
