import os
import numpy
import pandas
import csv
os.chdir("c:\\users\\abcd\\downloads")
f=open("data.csv","r")
data=csv.reader(f)
data=list(data)
print(data[0])
count=0
for i in data:
    if(i[20]=="Los Angeles Lakers"):
        count+=1
matches=count
action_type=[]
count=-1
for i in data:
    if(i[0] not in action_type):
        shot=i[0]
        count+=1
        action_type.append(shot)
action_type=action_type[1:]
#print(action_type)
action_types=count
#print(action_types)
shots=0
for i in data:
    if(i[14]=="1"):
        shots+=1
print("TOTAL SHOTS IN BUCKET "+str(shots))
all_shots=[]
for i in data:
    all_shots.append(i[0])
#print(all_shots)
shot_count={}
k=0
counter=0
for i in action_type:
    shot_count[i]=0
    if(i in all_shots):
            shot_count[i]=all_shots.count(i)
#print(shot_count)
correct_shot={}
right_shots=[]
for i in data:
    if(i[14]=="1"):
        right_shots.append(i[0])
#print(right_shots)
for i in action_type:
    correct_shot[i]=0
    if i in right_shots:
        correct_shot[i]=right_shots.count(i)
#print(correct_shot)
print(data[0])
data=numpy.array(data)
print(data.dtype)
#for i in data:
   # print(i[1])
shot_distance=[]
for i in data:
    if(i[14]=="1"):
        shot_distance.append(i[13])
#print(shot_distance)
shot_distance=numpy.array(shot_distance)    
shot_distance=shot_distance.astype(float)
#print(shot_distance)
print(numpy.unique(all_shots))
print(len(all_shots))
print(len(numpy.unique(all_shots)))
print((right_shots).map(data))
