s=input()
d=int(s.split()[0])
m=int(s.split()[1])
s2=input()
l1=s2.split()
l2=[]
for i in l1:
    l2.append(int(i))
count=0
rem=0
for i in range(len(l2)):
    if l2[i]<m:
        rem=l2[i]
        #count+=1
        continue
    elif l2[i]>=m:
        count+= l2[i]//m
        rem=l2[i]%m
        

    if i<len(l2)-1:
        if l2[i+1]+rem>=m:
            l2[i+1]=l2[i+1]+rem
        else:
            count+=1
    else:
        if rem>0:
            count+=1

print(count)