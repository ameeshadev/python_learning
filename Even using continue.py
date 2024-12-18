my_list=[12,8,9,5,6,3,18,16,11,19,14]
sum=0
for value in my_list:
    if value%2!=0:
        continue
    print(value,end=' ')
    sum+=value
else:
    print ("\n sum=",sum)
