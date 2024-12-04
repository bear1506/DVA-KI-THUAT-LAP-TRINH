print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
import numpy as np
#d.lieu dau vao
student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40., 42., 45., 41., 38., 40., 42.0]
#tao mang numpy tu d.lieu
student_data = np.array([student_id, student_height])
# sd lexsort de tang de s.xep ch.cao(tang dan)
#if c.cao=nhau thi id tang dan
sorted_indices = np.lexsort((student_id, student_height))
# In chi so sau khi s.xep
print("Chi so:")
print(sorted_indices)
# In d.lieu da sap xep
print("Du lieu sap xep:")
for i in sorted_indices:
    print("ID:", student_data[0, i], ", Chieu cao:", student_data[1, i])
