print("SV: ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
################################
def write_list_to_file(file_name, data_list):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  
        print(f"Nội dung đã được ghi vào tệp '{file_name}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi ghi vào tệp: {e}")
def main():
    file_name = input("Nhập tên tệp:")
    data_list = ['Đặng Việt Anh', 'KTDK-TDH', 'IG:bear15.6_']
    write_list_to_file(file_name, data_list)
if __name__ == "__main__":
    main()
