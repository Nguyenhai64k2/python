print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import turtle

# Tạo cửa sổ đồ họa
screen = turtle.Screen()
screen.bgcolor("white")  # Đặt nền cửa sổ thành màu trắng

# Tạo đối tượng turtle (rùa)
star = turtle.Turtle()
star.shape("turtle")  # Đặt hình dạng của rùa là "turtle"
star.color("blue")    # Đặt màu của con rùa thành màu xanh dương

# Tạo độ dày của bút vẽ
star.pensize(2)

# Vẽ ngôi sao 5 cánh
star.penup()  # Nhấc bút lên để di chuyển đến vị trí bắt đầu
star.goto(-50, 0)  # Di chuyển đến vị trí bắt đầu
star.pendown()  # Đặt bút xuống để bắt đầu vẽ

# Vẽ ngôi sao
for _ in range(5):  # Lặp lại 5 lần để vẽ các cạnh của ngôi sao
    star.forward(100)  # Vẽ một cạnh dài 100 đơn vị
    star.right(144)     # Quay phải 144 độ để tạo các góc của ngôi sao

# Ẩn con rùa sau khi vẽ xong
star.hideturtle()

# Đảm bảo cửa sổ không đóng ngay lập tức
turtle.done()
