print("SV Nguyen Dinh Hai ")
print("MSSV 2357520216100280")
print("#########################")
from tkinter import *

# Tạo cửa sổ chính
window = Tk()

# Thiết lập tiêu đề và kích thước cửa sổ
window.title("Thay đổi màu nền và màu chữ của Button")
window.geometry("400x300")

# Tạo nhãn (Label) hiển thị thông báo
lbl = Label(window, text="Nhấn nút bên dưới!", font=("Arial", 14))
lbl.pack(pady=20)

# Hàm xử lý khi nhấn nút
def on_button_click():
    lbl.configure(text="Bạn đã nhấn nút!")

# Tạo nút (Button) và thay đổi màu nền và màu chữ
btn = Button(window, text="Nhấn tôi!", command=on_button_click, bg="blue", fg="white", font=("Arial", 12))
btn.pack(pady=20)

# Chạy vòng lặp chính
window.mainloop()
