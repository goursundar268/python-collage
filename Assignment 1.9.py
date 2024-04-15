x=int(input("Enter the name:"))
for x in range(1,x+1):
    for y in range(1,x+1):
        print("*",end="")
    print("")
print("\n")

for x in range(1,x+1):
    for y in range(1,x+1):
        print(x,end="")
    print("")
print("\n")

for i in range(0,x+1):
    for y in range(0,i):
        print(chr(y+65),end="")
    print("")