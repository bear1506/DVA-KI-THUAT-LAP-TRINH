print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
def total_lines(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{file_name}'.")
        return 0
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return 0
def main():
    file_name = input("Nhập tên tệp: ")
    total = total_lines(file_name)
    print(f"Tổng số dòng trong tệp: {total}")
    n = int(input("Nhập số dòng bạn muốn đọc: "))
    read_first_n_lines(file_name, n)
if __name__ == "__main__":
    main()
