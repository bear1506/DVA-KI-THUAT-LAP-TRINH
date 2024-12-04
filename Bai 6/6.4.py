print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class RomanNumeral:
    def __init__(self, roman_num):
        self.roman_num = roman_num
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    def roman_to_int(self):
        num = 0
        prev = 0
        for i in range(len(self.roman_num) - 1, -1, -1):
            curr = self.roman_dict[self.roman_num[i]]
            if curr >= prev:
                num += curr
            else:
                num -= curr
            prev = curr
        return num
#vd:
roman_number = "MCMXCIV"
converter = RomanNumeral(roman_number)
result = converter.roman_to_int()
print(result)#Output:1994
