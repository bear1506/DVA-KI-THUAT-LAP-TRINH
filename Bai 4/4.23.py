print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def count_letters_and_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return letters, digits
sentence = input("Nhap mot cau:")
letters, digits = count_letters_and_digits(sentence)
print(f"So chu cai: {letters}")
print(f"So chu so: {digits}")
