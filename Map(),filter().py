#using map() function
#without lambda expression 
def multiply (value):
    return value**5
l1=[1,2,3,4,5]
l2=list(map(multiply,l1))
print (l1,l2)
#with lambda function
l1=[1,2,3,4,5]
l2=list(map(lambda value: value**5,l1))
print (l1,l2)
#using filter() function
#without lambda function
def is_divisible(value):
    if value%3==0:
        return value
l1=[1,2,3,4,5,6,7,8,9]
l2=list(filter (is_divisible,l1))
print (l1,l2)
#with lambda function
l1=[1,2,3,4,5,6,7,8,9]
l2=list(filter (lambda value:value%3==0,l1))
print (l1,l2)
