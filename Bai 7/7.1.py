print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def read_and_reverse_file(file_name):
    try:
        with open(file_name,'r') as file:
            content=file.readlines()
        reversed_content=content[::-1]    
        for line in reversed_content:
             print(line.strip())
    except FileNotFoundError:
         print(f"File'{file_name}'Khong ton tai.")
    except Exception as e:
         print(f"Co loi xay ra:{e}")
def main():
    file_name=input(f"Nhap ten file:")
    read_and_reverse_file(file_name)
if __name__=="__main__":
  main()
