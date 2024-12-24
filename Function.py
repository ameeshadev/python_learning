#python function
def display():
    ''' this is my first python function '''
    a,b=10,20
    c=a+b
    print ("sum=",c)
    print ("docstring=",display.__doc__)
display()
#with arguments and with return value
def power(x,n):
    p=x**n
    return p
x,n=map(int, input ("enter x and n").split())
print(f"{x} power {n}={power(x,n)}"
