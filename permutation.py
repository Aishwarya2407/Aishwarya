from itertools import permutations
n=input()
p=permutations(n)
for i in list(p):
     x=' '.join(i)
     print(x)
