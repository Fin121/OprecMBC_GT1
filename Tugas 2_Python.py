print("==Seragam Mahasiswa Telkom University==\n")
hari = str(input("Masukkan Nama Hari (tanpa kapital): \n"))

if (hari=='senin'):
    print("seragam hari senin adalah merah")
elif (hari=='selasa'):
    print("seragam hari selasa adalah putih")
elif (hari=='rabu'):
    print("seragam hari rabu adalah putih")
elif (hari=='kamis'):
    print("seragam hari kamis adalah bebas sopan")
elif (hari=='jumat'):
    print("seragam hari jumat adalah batik")
elif (hari=='sabtu'):
    print("seragam hari sabtu adalah bebas sopan")
else:
    print("anda tidak memilih hari")

# Assignmet MBC Meet 3 No 1
# Program for printing odd number from 1 to n

n = int(input('Please input the n value : '))
for i in range (n):
    if(i%2 != 0):
        print(i)


# Assignment MBC Meet 3 No 2
# Cashier Program

a = int(input(" Please input your total price :"))
b = input("Are you a member? (y/n")

if(500000<a<1000000):
    if(b == "y"):
        print("Congratulation you get","7%","discount")
    else:
        print("Congratulation you get","2%","discount")
elif(a>1000000):
    if(b == "y"):
        print("Congratulation you get","8%","discount")
    else:
        print("Congratulation you get","3%","discount")
else:
    if(b == "y"):
        print("Congratulation you get","5%","discount")
    else:
        print("Thank You!")
