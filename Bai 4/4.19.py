print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def sieve_of_eratosthenes(max_num):
    primes=[True]*max_num
    p=2
    while p**2 <= max_num:
        if primes[p]:
            for i in range(p**2,max_num,p):
                primes[i]=False
        p +=1
    return [p for p in range(2, max_num) if primes[p]]
p= tuple(sieve_of_eratosthenes(200))
print(p)
