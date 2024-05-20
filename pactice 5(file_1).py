import pickle
dic={}
fp=open("Student_data.dat","wb")
name=input("Enter name: ")
marks=int(input("Enter marks: "))
dic[name]=marks
pickle.dump(dic,fp)
