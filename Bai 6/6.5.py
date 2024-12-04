print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
class StringReverser:
    def __init__(self, string):
        self.string = string
    def reverse_words(self):
        words = self.string.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
#vd:
string = "hello .py"
reverser = StringReverser(string)
result = reverser.reverse_words()
print(result)
