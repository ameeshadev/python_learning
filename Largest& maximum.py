#create a new list with same numbers
l1=[int(x) for x in input("Enter l1 values").split()]
l2=[int(x) for x in input("Enter l2 values").split()]
l3=[]
for value in l1:
    if value in l2:
        l3.append(value)
        print (l3)
#largest number or maximum number
def find_max(my_list):
    max=my_list[0]
    for i in range(1,len(my_list)):
        if max<my_list[i]:
            max=my_list[i]
        return max
my_list=list(map(int,input("enter list values").split()))
print("Largest value=",find_max(my_list))
#count the maximum elements
my_list=list(map(int,input("Enter list value:").split ()))
count,max=1,my_list[0]
for i in range(1,len(my_list)):
    if my_list[i]>max:
        count+=1
        max=my_list[i]
print (count )
