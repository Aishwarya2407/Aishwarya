a=list(map(str,input().strip('.').split(' ')))
print(a)
d=[]
for i in a:
    b=len(i)
    d.append(b)
z=max(d)
x=min(d)
for i in a:
    if len(i)>=z:
        print("larger:",i)
    elif len(i)<=x:
        print("smaller:",i)
