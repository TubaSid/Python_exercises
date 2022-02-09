# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:38:57 2021

@author: teesid
"""
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
    print("It is an effin Armstrong number, Champ.")
else:
    print("Shu, you idiot. It's not what you think it is.")