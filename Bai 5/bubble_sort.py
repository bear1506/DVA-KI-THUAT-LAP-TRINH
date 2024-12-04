print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
#bubble_sort.py
def bubblesort(nlist):
    n=len(nlist)
    for i in range(n):
        swapped=False
        for j in range(n-1):
            if nlist[j] > nlist[j+1]:
                #traodoi
                nlist[j],nlist[j+1]=nlist[j+1],nlist[j]
                swapped=True
        #Neu khong can trao doi nua, thoat vong lap
        if not swapped:
            break
    return nlist
    
