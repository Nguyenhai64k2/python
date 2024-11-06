print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def generate_pascals_triangle(n):
    triangle = []  # Danh sách để chứa tam giác Pascal
    
    for i in range(n):
        row = [1]  # Mỗi dòng bắt đầu bằng 1
        for j in range(1, i):
            # Tính phần tử tại vị trí j của dòng i
            row.append(row[j - 1] * (i - j) // j)
        if i > 0:
            row.append(1)  # Mỗi dòng kết thúc bằng 1
        triangle.append(row)
    
    return triangle

# Nhập vào số n
n = int(input("Nhập số nguyên n: "))

# Tạo tam giác Pascal
pascals_triangle = generate_pascals_triangle(n)

# In ra tam giác Pascal
for row in pascals_triangle:
    print(" ".join(map(str, row)))
