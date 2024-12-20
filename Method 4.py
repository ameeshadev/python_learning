#capitalize()
#in method only the first letter is converted to capital the remains are small
s="python programming "
print (s.capitalize())
#find()
# it will return some integers index
print (s.find('h'))
# it will verify the sub string of string index
print(s.find('a',3,8))
print (s.find('z',4))
#it will return -1 because it is not in given string
#split()
# divides the string into list of substring
s="10,20,30,40,50"
print(s.split(','))
s="welcome to python"
print (s.split(' '))
#join
#in this method is reverse the split method
dob=['3','may','2006']
x='/'.join(dob)
print(x
