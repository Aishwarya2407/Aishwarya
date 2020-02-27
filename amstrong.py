import math
for i in range(20,1710):
    t=i
    d=int(math.log10(i))+1
    t=i
    c=0
    while(t>0):
       c+=(t%10)**d
       t=t//10
    if(c==i):
       print(i)
      
