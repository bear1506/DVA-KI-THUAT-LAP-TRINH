print("SV ĐẶNG VIỆT ANH")
print("MSSV:235752021610002")
##############################
#Ham nay cong hai so
def add (x, y):
  return x + y
#Ham nay tru hay so
def subtract(x, y):
  return x - y
#Ham nay nhan hai so
def multuply (x, y):
  return x * y
#Ham nay chia hai so
def divide (x, y):
  return x / y
print("Chon hoat dong:")
print("1.add")
print("2.subtract")
print("3.multuply")
print("4.divide")
choice = input ("Nhap lua chon phep tinh (1/2/3/4):")
numl = int(input("Nhap so dau tien: "))
num2= int(input("Nhap so thu hai: "))
if choice == '1':
  print (numl,"+",num2,"=", add(numl,num2))
elif choice == '2':
  print (numl,"-", num2,"=", subtract(numl, num2))
elif choice == '3':
  print (numl,"*", num2,"=", multuply(numl, num2))
elif choice == '4':
  print(numl,"/",num2,"=", divide(numl,num2))
else:
  print("Khong hop le: ")
