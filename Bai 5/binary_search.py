print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
#binary_search.py
def binary_search(sorted_list,value):
    lower_bound=0
    upper_bound=len(sorted_list)-1
    while lower_bound <= upper_bound:
        mid_point=(lower_bound+upper_bound) //2
        if sorted_list[mid_point] < value:
            lower_bound=mid_point+1
        elif sorted_list[mid_point] > value:
            upper_bound=mid_point -1
        else:
            return True
    
    
