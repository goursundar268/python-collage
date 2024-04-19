lst=[]
even=[]
odd=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        lst.append(int(num))
for i in lst:
   if i%2==0:
        even.append(i)
        
   else :
      odd.append(i)
    
print("Even number are",even)
print("The size of even number",len(even))

print("Odd number are",odd)
print("The size of odd number",len(odd))
