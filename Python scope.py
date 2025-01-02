#scopes in python
#a variable created inside the region is called scope
def myfunction():
    x=200
    print (x)
myfunction()    
# local variables can be accessed from a function  with in the function
def function():
    a=40
    def innerfunction():
        print(a)
    innerfunction()
function()    
#global variable created outside the function
b=33
def variable():
    print (b)
variable()    
print (b)
#naming variable it will be print local and global variables
a=300
def naming():
    a=400
    print(a)
naming()
print(a)
#nonlocal variable is a keyword the variable will belongs to outer function & inside nested function
def nonlocal1():
    x="ameesha"
    def nonlocal2():
        nonlocal x
        x="hello"
    nonlocal2()
    return x
print (nonlocal1())
    
