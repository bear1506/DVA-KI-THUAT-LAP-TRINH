print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
############################
S = input("Nhập chuỗi: ")
for char in S:
    if char not in (' ', '\t'):
        print(char.upper())
