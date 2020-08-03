# pattern 1
#n=4
# 1
  1 2 1
  1 2 4 2 1
  1 2 4 8 4 2 1
  *********************
  a=int(input())
for i in range(1,a):
    for i in range(0,i,1):
        print((2**i),end=" ")
    for i in range(-1+i,-1,-1):
        print((2**i),end=" ")
    print(" ")
