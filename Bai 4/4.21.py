print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def check_divisible_by_5(binary_numbers):
    binary_list = binary_numbers.split(',')
    result = []
    for binary in binary_list:
        try:
            if int(binary, 2) % 5 == 0:
                result.append(binary)
        except ValueError:
            print(f"Invalid binary number: {binary}")
    return ','.join(result)
input_data = "0100,0011,1010,1110"
output_data = check_divisible_by_5(input_data)
print(output_data)
