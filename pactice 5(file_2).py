import pickle
fp=open("Student_data.dat","rb")
data=pickle.load(fp)
print(data)