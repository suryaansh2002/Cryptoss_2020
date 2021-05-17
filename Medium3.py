from itertools import combinations 
s=input()
n=int(s.split()[0])
t=int(s.split()[1])
l=[]
for i in range(t):
    s2=input()
    left=int(s2.split()[0])
    right=int(s2.split()[1])
    l.append([left, right])
comb=combinations(l,len(l)-2)
l2=list(range(1,n+1))
l4=[]
for i in comb:
    for j in i:
        for k in range(j[0],j[1]+1):
            if k in l2:
                l2[l2.index(k)]=-1
    taught=l2.count(-1)
    l4.append(taught)
print(max(l4))
    

