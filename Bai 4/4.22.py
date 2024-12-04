print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def find_even_digit_numbers():
    result = []
    for number in range(1000, 3001):
        if all(int(digit) % 2 == 0 for digit in str(number)):
            result.append(str(number))
    return '.'.join(result)
output = find_even_digit_numbers()
print(output)
