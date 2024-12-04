print("SV: ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
################################
def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            num_lines = sum(1 for line in file)
            print(f"Số dòng trong tệp '{filename}': {num_lines}")
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
def main():
    filename = input("Nhập tên tệp:")
    count_lines_in_file(filename)
if __name__ == "__main__":
    main()
