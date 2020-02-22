from  math import sqrt
a=int(input())
flag=0
if sqrt(a)%1==0:
     flag=1
else:
    for i in  range(2,a//2+1):
        if(a%i==0 and sqrt(i)%1==0):
            flag=1
            break
if(flag==0):
        print("square free number")
else:
        print("not a square free number")
