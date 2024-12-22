#sets using union, intersection, difference,symmetric_difference
#union is denoted by/
a,b={1,2,3},{3,4,5}
c=a|b
#this is also a union 
c=a.union(b)
print(c)
#intersection is denoted by &
d=a&b
d=a.intersection(b)
print (d)
#difference is denoted by -
s1,s2={1,2,3},{5,8,9}
s3=s1.difference(s2)
s3=s1-s2
print(s3)
#symmetric_difference is denoted by ^
x,y={20,30,40,},{20,60,50}
z=x^y
z=x.symmetric_difference(y)
print(z
