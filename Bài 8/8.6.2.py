from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
def NewFile():
    text_widget.delete('1.0', END)
    print("Tệp tin mới đã được tạo!")
def OpenFile():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            text_widget.delete('1.0', END)
            text_widget.insert(END, content)
def SaveFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text_widget.get('1.0', END))
def Exit():
    root.quit()
def InsertText():
    text_widget.insert(END, "Đây là văn bản mới\n")
def InsertPicture():
    file_path = filedialog.askopenfilename(filetypes=[("Ảnh", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200))
        photo_image = ImageTk.PhotoImage(img)
        canvas.create_image(100, 100, image=photo_image)
# Tạo cửa sổ chính
root = Tk()
root.title("Trình soạn thảo văn bản")
# Tạo các widget
text_widget = Text(root, font=("Arial", 12))
text_widget.pack(fill="both", expand=True)
canvas = Canvas(root, width=200, height=200, bg="white")
canvas.pack(side="right", fill="y")
# Tạo menu
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Mới", command=NewFile)
filemenu.add_command(label="Mở", command=OpenFile)
filemenu.add_command(label="Lưu", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label="Thoát", command=Exit)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Chỉnh sửa", menu=editmenu)
editmenu.add_command(label="Chèn văn bản", command=InsertText)
editmenu.add_command(label="Chèn hình ảnh", command=InsertPicture)
#hiện thị
root.mainloop()
