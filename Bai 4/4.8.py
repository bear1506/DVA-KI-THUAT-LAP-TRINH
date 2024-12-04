print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
############################
def tu_dai_nhat(s):
    tuDaiNhat=""
    dsCacTu=s.split()
    for tu in dsCacTu:
        if(len(tu)>len(tuDaiNhat))or (len(tuDaiNhat)and tu<tuDaiNhat):
            tuDaiNhat = tu
    return tuDaiNhat                              
s=input() 
print(tu_dai_nhat(s))
