print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def filter_odd_numbers(numbers_string):
    numbers_list = [int(num) for num in numbers_string.split()]
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    return odd_numbers
input_data = input("Nhap danh sach cac so:")
filtered_data = filter_odd_numbers(input_data)
print(' '.join(map(str, filtered_data)))
