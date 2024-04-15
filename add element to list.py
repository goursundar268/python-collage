list=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        list.append(int(num))
x=int(input("The element of seach:"))
if num in list:
    print("the number of found of this list")
else:
    print("the number of not found of this list")
    
    y=int(input("Add element yes(1)/No(0)::"))
    if y==1:
        list.append(y)
        print("Add succesfully")
        print(list)
    elif y==0:
        list.append(y)
        print("no Added")
       
    else:
        print("Invild")
        
    