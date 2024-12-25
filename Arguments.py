#types of arguments
#1.required or positional argument
def display (a,b,c):
    print(a,b,c)
display(1,2,3)
#this is valid conclusion
#display(1,2)and display(1,2,3)
#this arguments are passing the values it can be taken by given values
def intrest (p=1000,t=12,r=2.6):
    print("intrest=",(p*t*r)/100)
    intrest ()
    intrest (2000)
    intrest(5000,24)
    interest (4000,4,6)
    #the output wil be diplay in this way
 #intrest= 312.0
 #intrest= 624.0
 #intrest=3120.0
 #intrest=960.0
 
