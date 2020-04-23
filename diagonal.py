a=input()
for i in range(0,len(a)): 
     j = len(a)-1 - i 
     for k in range(0, len(a)): 
          
        if (k == i or k == j): 
            print(a[k],end = "") 
        else: 
            print(end = " ") 
     print()  
