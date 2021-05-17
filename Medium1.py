from itertools import permutations 
s=input()
m=int(s.split()[0])
b=int(s.split()[1])
l=[]
for i in range(b):
    s2=input()
    l3=[]
    for i in s2.split():
        l3.append(int(i))
    l.append(l3)
perm=permutations(list(range(1,b+1)))
l2=[]
for i in perm:
    l2.append(list(i))
l4=[]
for i in l2:
    l3=list(range(1,m+1))
    frustrate=0
    for j in i:
        a=l[j-1]
        if a[0] in l3 and a[1] in l3:
            l3.pop(l3.index(a[0]))
            l3.pop(l3.index(a[1]))
        elif a[0] in l3:
            l3.pop(l3.index(a[0]))
        elif a[1] in l3:
            l3.pop(l3.index(a[1]))
        else:
            frustrate+=1
    l4.append(frustrate)
    frustrate=0


print(min(l4))
