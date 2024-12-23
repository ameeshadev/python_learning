#dictionary is a collection of key:value pairs
# dictionary using{}
student={"rno":5,"name":"ameesha","age":19}
print(student)
# dictionary using dict() this is constructer or function
students=dict([("rno",5),("name","friends"),("age",33)])
print(students)
#dictionary using empty
students=dict()
print(students)
#using dictionary comparison
d={x:x**3 for x in range(1,11) if x%2==0}
print(d)
#how to access individual values in dictionary
a={1:'a',2:'b',3:'c',4:'d',1:'e'}
#in this dictionary we have two keys are same but values are different but it first key to update the second key it will come 1 key is e
print (a[1])
print(a[3])
print(a[4])
