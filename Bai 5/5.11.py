print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
import numpy as np
#dinh nghia kieu du lieu c.truc cho mang c.truc
data_type=[('name','S4'),('class',int),('height',float)]
#du lieu sv
students_details=[
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5,42.10),
    ('Pit', 5, 40.11)
]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")

sorted_students=np.sort(students, order='height')
print(sorted_students)
