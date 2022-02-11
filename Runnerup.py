arr = [2,3,6,6,5]

array=[]
array=list(dict.fromkeys(arr))
n=len(array)
for j in range(n):      
    for i in range(j):
        if array[i]>array[j]:
            c=array[j]
            array[j]=array[i]
            array[i]=c

array.reverse()
if len(array)<2:
    print(array[0])
else:
    print(array[1])

