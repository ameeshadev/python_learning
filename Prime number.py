x,y=map(int, input ("enter x&y values ").split())
for i in range(x,y+1):
    found=False
    for j in range(2,i):
        if i%j==0:
            found=True
            break
    if found==False:
        print(i,end='')
