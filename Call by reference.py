#call by reference
def update (name):
    name='hi'+name
    print (" in subfunction,name=",name)
name="python"
update(name)
print ("in main, name=",name)
#on mutable objects it behavious a pass by reference
def number (my_list):
    my_list.append(100)
    my_list.append(200)
    my_list=[10,20,30,40,50]
    print ("before call,list=",my_list)
    number (my_list)    
    print ("after call,list=",my_list)
    #before call,list= [10, 20, 30, 40, 50]
    #after call,list= [10, 20, 30, 40, 50, 100, 200]
#un packing arguments
def display(a,b,c,d):
    print(a,b,c,d)
l=[10,20,30,40]
display(*l)   
#output is 10 20 30 4
