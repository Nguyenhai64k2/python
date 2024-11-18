print("SV Nguyen Dinh Hai")
print("MSSV 235752021610028")
print("#######################")
import turtle

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Đặt màu nền của cửa sổ

# Tạo đối tượng rùa (turtle)
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")  # Đặt hình dạng của con rùa là "turtle"
my_turtle.color("green")   # Đặt màu cho con rùa

# Vẽ một hình vuông
my_turtle.penup()  # Nhấc bút lên (không vẽ khi di chuyển)
my_turtle.goto(-100, 100)  # Di chuyển đến vị trí bắt đầu
my_turtle.pendown()  # Đặt bút xuống để vẽ

for _ in range(4):
    my_turtle.forward(200)  # Vẽ một cạnh của hình vuông
    my_turtle.right(90)      # Quay 90 độ để vẽ các cạnh còn lại

# Vẽ một hình tròn
my_turtle.penup()  # Nhấc bút lên
my_turtle.goto(100, -100)  # Di chuyển đến vị trí vẽ hình tròn
my_turtle.pendown()  # Đặt bút xuống để vẽ

my_turtle.circle(100)  # Vẽ một hình tròn với bán kính 100

# Ẩn con rùa sau khi vẽ xong
my_turtle.hideturtle()

# Đảm bảo cửa sổ không đóng ngay lập tức
turtle.done()
