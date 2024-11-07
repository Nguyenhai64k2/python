print("Nguyen Dinh Hai")
print("MSSV: 235752021610028")
print("############################")
class RomanToInt:
    def __init__(self):
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, roman):
        total = 0
        for i in range(len(roman)):
            current_value = self.roman_values[roman[i]]
            if i + 1 < len(roman) and current_value < self.roman_values[roman[i + 1]]:
                total -= current_value  
            else:
                total += current_value 
        return total
roman_converter = RomanToInt()
roman_number = input("Nhập số La Mã: ").upper()
result = roman_converter.convert(roman_number)
print(f"Số nguyên tương ứng là: {result}")
