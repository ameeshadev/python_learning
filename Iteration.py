#iterating loops
#for loop: using repeated values
a="string name"
for i in a:
    print (a)
#using range
for i in range(0,10,2):
    print (i)
#else condition for loop
for i in range(1,6):
    print (i)
else:
    print ("numbers are  printed one by one")
#continue statement
# Prints all letters except 'e' and 's'
for i in 'ameesha':
    if i == 'e' or i == 's':
        continue
    print(i) 
#break statement
names=["ammulu","honey","kamal"]
for i in names:
    if i=="kamal":
        break 
    print(i)
