a=int(input())
f=0
f1=1
for i in range(2,a+1):
    f2=f+f1
    f=f1
    f1=f2
print(f2)
