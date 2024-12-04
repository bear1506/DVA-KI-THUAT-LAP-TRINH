print("SV:ĐẶNG VIỆT ANH")
print("MSSV: 235752021610002")
################################
def count_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            num_lines = len(content)
            num_words = 0
            num_characters = 0
        for line in content:
                num_characters += len(line)
                num_words += len(line.split())
        print(f"Số dòng: {num_lines}")
        print(f"Số từ: {num_words}")
        print(f"Số ký tự: {num_characters}")
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
def main():
    file_name = input("Nhập tên file:")
    count_file_contents(file_name)
if __name__ == "__main__":
        main()
