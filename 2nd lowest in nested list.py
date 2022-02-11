# Who has the second lowest marks?

name=[]
score=[]
for i in range(int(input("Enter number of students: "))):
        name.append(input("Enter name: "))
        score.append(float(input("Enter score: ")))

l=0
n=len(name)
idx=0
index=0
sort=[]

for i in range(n):
    for j in range(i):
        if score[i]<score[j]:
            c=score[i]
            score[i]=score[j]
            score[j]=c
            p=name[i]
            name[i]=name[j]
            name[j]=p
for i in range(n):
    for j in range(i):
        if l<1:
            if score[0]!=score[i:i+1]:
                l+=1
                idx=i
                v=score[i];
        if score[idx:idx+1]<score[i:i+1]:
            index=j  
if score[idx:idx+1]==score[index-1:index]:
    for i in range(idx,index):
        sort.append(str(name[i]))
else:
    print(name[idx])
sort.sort()
for i in range(len(sort)):
    print(sort[i]," has the second lowest marks.")
