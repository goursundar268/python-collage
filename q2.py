
menu={
    1 : "Addition",
    2 : "Substraction",
    3 : "Multiplication",
    4 : "Division",
    5 : "Reminder",
    6 : "Quotient",
    7 : "Exporent"
}
for i in menu:
    print(i,menu[i])
ch=int(input("Enter your choice::"))
a=int(input("Enter the Number1::"))
b=int(input("Enter the Number2::"))

if ch==1:
    r1=a+b
    print(f"Addition of {a} and {b} is {r1}")
elif ch==2:
    r1=a-b
    print(f"substraction of {a} and {b} is {r1}")
elif ch==3:
    r1=a*b
    print(f"multiplication of {a} and {b} is {r1}")
elif ch==4:
    r1=a/b
    print(f"division of {a} and {b} is {r1}")
elif ch==5:
    r1=a%b
    print(f"reminder of {a} and {b} is {r1}")
elif ch==6:
    r1=a//b
    print(f"quotient of {a} and {b} is {r1}")
elif ch==7:
    r1=a**b
    print(f"Expoent of {a} and {b} is {r1}")
else :
    print("sorry:: wong operator")
print("Thank you for using it \n this is created by gour")
