n=int(input("enter n"))
sf,i=0,1
while i<n:
    if n%i==0:
        sf=sf+1
        i=i+1
else:
    print("perfect") if sf==n else print("not
