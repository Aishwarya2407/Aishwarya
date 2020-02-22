a=input()
c=a.count("@")
if c==1:
   b=a.index("@")
   if b>6:
       d=a[b+1:]
       e=len(d)
       if e>3:
          s=a.index(".")
          if (a.endswith(".com")):
              print("valid")
else:
    print("invalid")
    
    
