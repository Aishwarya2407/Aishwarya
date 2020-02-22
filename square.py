a=int(input())
b=[]
for i in range(0,a//2):
    b.append(2**i)
    b.append(3**i)
print(b[a-1])
