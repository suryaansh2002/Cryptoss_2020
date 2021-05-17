N=int(input())
s=input()
l1=s.split()
l2=[]
l3=[]
if len(l1)==N:
    for i in l1:
        l2.append(int(i))
    l2.sort()
    for i in range(N-2):
        if l2[i]+l2[i+1]>l2[i+2]:
            l3.append((l2[i],l2[i+1],l2[i+2]))
    if len(l3)>0:
        print("YES")
        print(l3[-1][2],l3[-1][1], l3[-1][0])
    else:
        print("NO")
    