a=int(input())
for i in range(2,a):
    while(a%i==0):
        print(i,end=" ")
        a/=i

output:
12
2 2 3
