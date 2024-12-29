#algorithms
#linear search
#defining a function
def linear_search(array,x):
    for i in range (len(array)):
      if array[i]==x:
          return i
    return -1
array=[10,50,40,33,44]   
print(f"Array={array}")
x=33
index=linear_search(array,x)
if index!=-1:
    print(f"the given element {x} is present at the index{index}.")
else:
  print(f"the given element {x} is not present at the index",str(index))
