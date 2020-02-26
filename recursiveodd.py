i=0
def odd(n):
    global i
    if(i<n):
       print(2*i+1)
       i=i+1
       odd(n)
    if(i==n):
       i=0 
n=int(input())
odd(n)

