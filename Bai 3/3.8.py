print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
##############################
import math
pos = [0,0] 
while True:
  s = input () 
  if not s:
    break
  movement = s.split(" ")
  direction = movement [0]
  steps = int (movement [1]) 
  if direction=="UP":
    pos[0]+=steps
  elif direction=="DOWN":
    pos[0]-=steps
  elif direction=="LEFT":
    pos[1]-=steps
  elif direction=="RIGHT":
    pos [1]+=steps
  else:
      pass
   ###########################
distance= math.sqrt(pos[1]**2 + pos[0]**2)
print (int (distance))
