#variable length we can assign mixed argument
def display(x,*v):
    print("x=",x)
    print("v=",v)
display (1,2,3,4,5)
display (10,20,30)
display ('a')
#we can't assign display () is empty so we can assign at least one value can assign
#variable length keyword
def display (**kwargs):
    print (kwargs)
display (rno=101,name="ravi",branch="cse")    
display (name="ravi",branch="IT")
display ()
