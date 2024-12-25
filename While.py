#while loop
a=0
while (a<3):
    print ("hello")
    a=a+1
#by using continue statements
# Prints all letters except 'e' and 's'
i = 0
while i < 10:
    if i == 'e' or i == 's':
        i += 1
        continue
        
    print(i)
    i += 1
#by using break statement
i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
        
    print(i)
    i += 1
