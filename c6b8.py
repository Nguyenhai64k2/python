print("SV Nguyen Dinh Hai ")
print("MSSV 2357520216100280")
print("#########################")
from tkinter import *
from tkinter import messagebox

# Hàm xử lý cho mục "New" trong menu File
def NewFile():
    print("New File!")
    lbl.config(text="New File!")  # Hiển thị thông báo trên Label

# Hàm xử lý cho mục "Open" trong menu File
def OpenFile():
    print("Open File!")
    lbl.config(text="Open File!")  # Hiển thị thông báo trên Label
    messagebox.showinfo("Open File", "You selected Open File")  # Hiển thị hộp thoại thông báo

# Hàm xử lý cho mục "Exit" trong menu File
def Exit():
    print("Exit!")
    lbl.config(text="Exiting application...")  # Hiển thị thông báo trên Label
    root.quit()  # Thoát chương trình

# Hàm xử lý cho mục "Text" trong menu Insert
def InsText():
    print("Insert Text!")
    lbl.config(text="Text Inserted!")  # Hiển thị thông báo trên Label
    messagebox.showinfo("Insert Text", "You selected Insert Text")  # Hiển thị hộp thoại thông báo

# Hàm xử lý cho mục "Picture" trong menu Insert
def InsPic():
    print("Insert Picture!")
    lbl.config(text="Picture Inserted!")  # Hiển thị thông báo trên Label
    messagebox.showinfo("Insert Picture", "You selected Insert Picture")  # Hiển thị hộp thoại thông báo

# Tạo cửa sổ chính
root = Tk()
root.title("Menu Example with Tkinter")  # Đặt tiêu đề cho cửa sổ

# Tạo một menu bar
menu = Menu(root)
root.config(menu=menu)

# Tạo menu "File"
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)  # Mục "New"
filemenu.add_command(label="Open", command=OpenFile)  # Mục "Open"
filemenu.add_separator()  # Thêm dấu phân cách
filemenu.add_command(label="Exit", command=Exit)  # Mục "Exit" để thoát chương trình

# Tạo menu "Insert"
insertmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)  # Mục "Text"
insertmenu.add_command(label="Picture", command=InsPic)  # Mục "Picture"

# Tạo menu "Help"
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=lambda: messagebox.showinfo("About", "This is a simple example of a menu"))  # Mục "About..."

# Tạo một Label để hiển thị thông báo
lbl = Label(root, text="Select an option from the menu", font=("Helvetica", 14))
lbl.pack(padx=20, pady=20)

# Chạy vòng lặp chính để hiển thị giao diện
root.mainloop()

