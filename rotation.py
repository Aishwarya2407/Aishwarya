a=int(input())
z=int(input())
b=[]
for i in range(1,a+1):
    c=int(input())
    b.append(c)
print(b)
for i in range(0,z):
    b=b[-1:]+b[0:a-1]
    print(b)
