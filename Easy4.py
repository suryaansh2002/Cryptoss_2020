n=int(input())
s=input()
s2=s
if len(s)==n:
    while '01' in s:
            s=s[:s.index('01')]+s[s.index('01')+2:]
    print(len(s))