a=list(map(int,input().split()))
print(a)
d=[]
for i in range(0,len(a)):
     c=a.count(a[i])
     d.append(c)
print(d)
for i in range(0,len(d)):
     if d[i]>1:
         print(d[i])
         break
     

