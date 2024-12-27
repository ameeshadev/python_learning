#decorator chaining
def decorator1(divide):
    def inner1(a,b):
        if a<b:
            divide(b,a)
        else:
            divide(a,b)
    return inner1
def decorator2(divide):
    def inner2(a,b):
        if b==0:
            print ("b can't zero")
            b=int(input(" enter b value"))
        divide(a,b)
    return inner2
@decorator1
@decorator2
def divide(a,b):
    print ("result=",a/b)
divide(20,6)    
divide(8,45)
divide(16,0)
