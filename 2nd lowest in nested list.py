l=0
idx=0
index=0
sort=[]
nested_list=[]
for i in range(int(input("Enter no. of students: "))):
        name=(input("Enter name: "))
        score=(float(input("Enter score:")))
        nested_list.append([name,score])
n=len(nested_list)
for i in range(n):
    for j in range(i):
        if nested_list[i][1]>nested_list[j][1]:
            c=nested_list[i]
            nested_list[i]=nested_list[j]
            nested_list[j]=c
nested_list.reverse()
for i in range(n):
    for j in range(i):
        if l<1:
            if nested_list[0][1]!=nested_list[i][1]:
                l+=1
                idx=i
                v=nested_list[i][1];
        if nested_list[idx][1]==nested_list[i][1]:
            index=i
if nested_list[idx][1]==nested_list[index][1]:
    for i in range(idx,index+1):
        sort.append(str(nested_list[i][0]))
else:
    print(nested_list[idx][0])
sort.sort()
for i in range(len(sort)):
    print(sort[i],"has the second lowest marks.")
