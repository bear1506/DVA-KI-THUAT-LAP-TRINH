print("Sv:Đặng Việt Anh")
print("MSSV:235752021610002")
##############################
def tam_giac_pascals(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def main():
    n = int(input("Nhap so dong cua tam giac Pascals: "))
    triangle = tam_giac_pascals(n)
    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
