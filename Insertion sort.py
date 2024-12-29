#sorting
#insertion sort
def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        c=i-1
    while c>=0 and key<array[c]:
        array[c+1]=array[c]
        c-=1
        array[c+1]=key
array=[23,42,3,83,36,49,19]
print ("unsorted array:", array)
insertion_sort(array)
print("sorted array:",array)
