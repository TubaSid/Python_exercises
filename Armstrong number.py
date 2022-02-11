
#calculate
ans=0
num=input()
p=len(num)   
for i in str(num):
    ans=ans+(int(i)**p)
print(ans)
#is it armstrong?
num=int(num)
if ans==num:
    print("It is an Armstrong number, Champ.")
else:
    print("Shu, It's not what you think it is.")
