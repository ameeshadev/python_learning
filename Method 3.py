#replace()
#to replace a new character an old character
s="abcadefagah"
s1=s.replace('a','#')
s2=s.replace('a','@',2)
#2 refers first two values
print(s1)
print(s2)
# swapcase()
#it will converts to  upper case to lower case and contains only alphabet are converted
s="abxy"
s1=s.swapcase()
print (s1)
#count()
# it can be using multiple arguments
s="abcadeyefhjkdvbn"
r=s.count('a')
d=s.count('a',5)
#5 returns starting 5 th index
e=s.count('a',3,7)
# it will be retuns 3 index to 7 index
print(r)
print(d)
print(e)
