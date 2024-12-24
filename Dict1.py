#methods of dictionary
#copy()
a={"class":"cse","section":'d',"rno":321}
b=a.copy()
print(a)
#items()
item=[("rno",101),("name","ravi"),("marks",80)] 
print(item)
#keys
keys=["rno","name","marks"]
print(keys)
values=[101,"ravi",80]
print(values)
#fromkeys(keys, value )
#create a new dictionary we can use this
keys=(1,2,3,4)
value="ameesha"
d=dict.fromkeys(keys,value)
print(d)
#setdefault(key,value)
d={1:'a',2:'b',3:'c'}
d.setdefault(4,'d')
#this one is added to dict
print(d
