print("SV: ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
##############################
import tkinter as tk
#Phương thức xử lý sự kiện phím bấm
def key_pressed(event):
    print("Key pressed:",event.keysym)
#Toạ một cửa sổ đồ hạo
window=tk.Tk()
#Thiết lập tiêu đề cửa sổ
window.title("VIETANH")
#thiết lập kích thước của sổ
window.geometry("350x200")
#Gắn phương thức xử lí sự kiện phím bấm vào cửa sổ
window.bind("<Key>",key_pressed)
#hiện thị
window.mainloop()
