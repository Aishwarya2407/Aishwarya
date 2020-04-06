n=int(input())
c=0
while n>0:
    u=n%10
    if u%2==1:
        c+=u
    n=int(n/10)
print(c)
    
