print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
# sequential_search.py
def Sequential_search(dlist,item):
    for i in range(len(dlist)):
        if dlist[i]==item:
            return (True,i)
    return (False,-1)    
