#lambda or anonymous function
#normal function 
def power(x,n):
    return x**n
x,n=2,5
print (f"{x} power {n}={power(x,n)}")
#anonymous fonction
#syntax:lambda parameters: expression
x,n=2,5
power=lambda x,n:x**n
#power is assigning to all syntax
print (f"{x} power {n}={power(x,n)}")
#big number is assigning
#without function 
def big(a,b):
    return a if a>b else b
a,b=10,20
print ("big=",big(a,b))
#with function
a,b=10,20
big=lambda a,b:a if a>b else b
#if and else is not a condition statement
print ("big=",big(a,b))
