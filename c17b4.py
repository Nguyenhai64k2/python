print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def tong_uoc(x):
    tong = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:  # i là ước của x
            tong += i
            if i != x // i:  # tránh cộng ước trùng
                tong += x // i
    return tong

# Nhập số n
n = int(input("Nhập số n: "))

# In các số có tổng ước số lớn hơn chính nó
for x in range(1, n):
    if tong_uoc(x) > x:
        print(x)
