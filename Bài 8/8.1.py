print("SV: ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
################################
import turtle
# Tạo cửa sổ vẽ và rùa(turtle)
window = turtle.Screen()
window.bgcolor("yellow")
painter = turtle.Turtle()
painter.color('red')
painter.pencolor('red')
painter.pensize(3)
# Vẽ một hình vuông
def drawsq(t, s):
   for i in range(4):
       t.forward(s)
       t.left(90)
for i in range(1,180):
    painter.left(18)
    drawsq(painter,200)
