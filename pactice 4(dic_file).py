import pickle
dic={}
fp=open("Student_data.dat","wb")
while True:
    keys=input("Enter a student Name:")
    if keys in dic:
        print("Student name is alradey here:-")
        print("Enter 0(zero) press end dictinory")
    elif keys=="0":
        break
    else:
        value=int(input("Enter the student marks::"))
        dic[keys]=value
        print(f"{keys} {value} marks added in dictinory")
        

pickle.dump(dic,fp)
fp=open("Student_data.dat","rb")
data=pickle.load(fp)
print(data)
