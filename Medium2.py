n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
s=''
for i in l:
    s+=i
print(s.count('ab')*10)