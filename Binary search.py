#algorithms
#binary search
#defining a function
def binary_search(array,x):
    lower=0
    higher=len(array)-1
    middle=0
    while lower<=higher:
        middle=(higher+lower)//2
        if array[middle]<x:
            lower=middle+1
        elif array[middle]>x:
            higher=middle-1
        else:
            return middle
    return -1
array=[10,50,40,33,44]    
x=33
index=binary_search(array,x)
print (f"Array={array}")
if index!=-1:
    print(f"the given element {x} is present at the index{index}.")
else:
  print(f"the given element {x} is not present at the index",str(index))
