r=2
c=2
b=[[0 for i in range(r)]for j in range(c)]
for i in range(0,r):
     for j in range(0,c):
        b[i][j]=int(input())
for i in range(0,r):
    for j in range(0,c):
        print(b[i][j],end=" ")
    print(" ")
        

        
        
