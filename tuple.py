#tuples 
#tuples is a immutable
t1=(10,20,30,40,50)
t3=1,2,3,4,5
t4=t1+t3
print(t4)
#we can add this numbers also
t2=tuple(t1)
print(t2)
s="python"
k=tuple(s)
print(k)
#we can use strings also
#tuple packing
a=(12,34,45,56,67,78,89)
print(a)
#tuple unpacking
b=(33,55,22,80,30)
a,*b,c=b
print(b)
