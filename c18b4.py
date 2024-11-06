print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def fibonacci_less_than_n(n):
    fib_list = []
    a, b = 0, 1  # Các số Fibonacci đầu tiên
    
    while a < n:
        fib_list.append(a)  # Thêm số Fibonacci vào danh sách
        a, b = b, a + b  # Cập nhật các số Fibonacci tiếp theo
    
    return fib_list

# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Tạo và in ra danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = fibonacci_less_than_n(n)
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_numbers)
