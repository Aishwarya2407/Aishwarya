a=int(input())
b=list(map(int,input().split()))
c=[]
f=[]
for i in b:
    d=bin(i)
    c.append(d)
print(c)
for j in c:
    f.append(j.count("1"))
print(f.index(max(f)))
    
