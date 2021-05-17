s=input()
n=int(s.split()[0])
m=int(s.split()[1])
s=input()
l=[]
for i in s.split():
    (l.append(int(i)))
s=input()
l2=[]
for i in s.split():
    (l2.append(int(i)))
c=0
for i in range(len(l2)):
    if l2[i]==1:
        c+=l[i]
    else:
        continue
count = c
while 0 in l2:
    try:
        c=count
        first=l2.index(0)
        for i in range(first, first+m+1):
            if l2[i]==0:
                l2[first]=1
                c+=l[i]
    except:
        break
print(c)