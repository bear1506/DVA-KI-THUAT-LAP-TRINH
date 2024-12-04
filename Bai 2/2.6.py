print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
result = [] 
for i in range(2000, 3201): 
    if (i % 7 == 0) and (i % 5 != 0):  
        result.append(str(i)) 
print(", ".join(result))
