print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import turtle

# Khởi tạo cửa sổ đồ họa
screen = turtle.Screen()
screen.bgcolor("white")  # Đặt nền cửa sổ thành màu trắng

# Tạo đối tượng turtle để vẽ các hình tròn
circle_turtle = turtle.Turtle()
circle_turtle.shape("turtle")  # Đặt hình dạng của rùa là "turtle"
circle_turtle.speed(10)  # Tăng tốc độ vẽ

# Hàm vẽ một hình tròn
def draw_circle(radius, color, angle):
    circle_turtle.penup()
    circle_turtle.goto(0, -radius)  # Di chuyển con rùa đến vị trí vẽ hình tròn (dưới vị trí gốc)
    circle_turtle.pendown()
    circle_turtle.color(color)  # Đặt màu cho hình tròn
    circle_turtle.setheading(angle)  # Quay rùa đến góc tương ứng
    circle_turtle.circle(radius)  # Vẽ hình tròn

# Vẽ 12 hình tròn giao nhau tại cùng một điểm
radius = 50  # Bán kính của các hình tròn

# Vẽ 4 hình tròn màu xanh nước biển (xanh dương)
for i in range(4):
    angle = i * 90  # Các góc quay cách nhau 90 độ để các hình tròn giao nhau tại cùng một điểm
    draw_circle(radius, "blue", angle)

# Vẽ 4 hình tròn màu xanh lá cây
for i in range(4):
    angle = 45 + i * 90  # Góc quay cho nhóm màu xanh lá cây (chệch 45 độ so với nhóm màu xanh nước biển)
    draw_circle(radius, "green", angle)

# Vẽ 4 hình tròn màu đỏ
for i in range(4):
    angle = 22.5 + i * 90  # Góc quay cho nhóm màu đỏ (chệch 22.5 độ so với nhóm màu xanh lá cây)
    draw_circle(radius, "red", angle)

# Đảm bảo cửa sổ không đóng ngay lập tức
turtle.done()
