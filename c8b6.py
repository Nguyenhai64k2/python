print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        """Kiểm tra mã PIN người dùng nhập vào."""
        return self.pin == entered_pin

    def check_balance(self):
        """Hiển thị số dư tài khoản."""
        return self.balance

    def deposit(self, amount):
        """Nạp tiền vào tài khoản."""
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} vào tài khoản. Số dư hiện tại: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        """Rút tiền từ tài khoản."""
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        elif amount > self.balance:
            print("Số dư không đủ để rút.")
        else:
            self.balance -= amount
            print(f"Đã rút {amount}. Số dư hiện tại: {self.balance}")

# Tạo đối tượng ATM với mã PIN và số dư ban đầu
atm = ATM(pin="1234", balance=1000)

# Xác thực người dùng bằng PIN
entered_pin = input("Nhập mã PIN: ")

if atm.check_pin(entered_pin):
    print("Xác thực thành công!")
    
    while True:
        print("\n------ Menu ATM ------")
        print("1. Kiểm tra số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")
        
        choice = input("Chọn một hành động (1/2/3/4): ")

        if choice == '1':
            print(f"Số dư tài khoản của bạn: {atm.check_balance()}")

        elif choice == '2':
            amount = float(input("Nhập số tiền cần nạp: "))
            atm.deposit(amount)

        elif choice == '3':
            amount = float(input("Nhập số tiền cần rút: "))
            atm.withdraw(amount)

        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
            break  

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
else:
    print("Mã PIN không đúng. Vui lòng thử lại.")

