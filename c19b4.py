print ("sinh vien Nguyen Dinh HAi ")
print ("mssv 235752021610028")
print ("############################")
def sieve_of_eratosthenes(limit):
    # Khởi tạo mảng đánh dấu các số nguyên tố
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 và 1 không phải là số nguyên tố
    
    # Dùng Sàng Eratosthenes để đánh dấu các số nguyên tố
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Trả về các số nguyên tố nhỏ hơn limit
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    
    return tuple(primes)

# Nhập vào số nguyên n từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Tạo tuple P gồm các số nguyên tố nhỏ hơn n
P = sieve_of_eratosthenes(n)

# In ra tuple các số nguyên tố
print("Tuple các số nguyên tố nhỏ hơn", n, "là:", P)


