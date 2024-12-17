n=int(input("enter n"))
found,i=False,2
while i<n:
    if n%i==0:
        found=False
        break
        i=i+1
    else:
        print("else block")
    if found==False:
        print("prime")
    else:
        print(" not a prime")
        
    
