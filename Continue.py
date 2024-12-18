my_list=[12,8,9,5,6,3,18,16,11,19,14]
sum=0
# this sum value store the even number 
for value in my_list:
    # iterating my_list function 
    if value%2!=0:
        # value is odd the continue statement skips the rest of the code is iteration and moves to the next value
        continue
    print(value,end=' ')
    #if the value is even so it will be print 
    sum+=value
else:
    print ("\n sum=",sum
