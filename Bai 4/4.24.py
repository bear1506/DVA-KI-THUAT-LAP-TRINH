print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def count_upper_and_lower_case(sentence):
    upper_case=sum(1 for c in sentence if c.isupper())
    lower_case=sum(1 for c in sentence if c.islower())
    return upper_case, lower_case
sentence=input ("Nhap mot cau")
upper_case, lower_case= count_upper_and_lower_case(sentence)
print(f"chu hoa:{upper_case}")
print(f"chu thuong:{lower_case}")
