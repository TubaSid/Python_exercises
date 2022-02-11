
import re
if __name__ == '__main__':
    #S=input('enter')
    #k=input("enter")
    S="aaaddaa"
    k="aa"
    t=0
    f=0
    j=[]
    l=[]
    pl=[]
    i=0
    e=len(k)-1
    m = re.search(r'\w+',k)
    st=m.start()
    en=m.end()
    n=len(S)
    for i in range(n):
        if k[st]==S[i]:
            j.append(i)
            for i in range(n):
                if e==0:
                    i=i
                else:
                    i+=1
                if i<n:
                    if k[en-1]==S[i]:
                        l.append(i)
                        f=1
        
    jj=j[0]
    c=0
    u=len(j)
    if f==1:
        for i in range(u):
            for sz in range(u):
                if c==0 & j[sz]==j[0]:
                    c+=1
                    if (l[i]-j[sz])==abs(e):
                        print("("+str(j[sz])+", "+str(l[i])+")")
                elif j[sz]!=jj:
                    if (l[i]-j[sz])==abs(e):
                        print("("+str(j[sz])+", "+str(l[i])+")")

    else:
            print("(-1,-1)")            
        
    
