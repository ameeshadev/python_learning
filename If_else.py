#build caluclator
a=int(input("enter number1:_"))
b=int(input("enter number2:_"))
c=int(input("enter number3:_"))
d=int(input("enter number4:_"))
A=input("enter a method:_").upper()
if(A=="ADD"):
	print(a+b+c+D)
elif(A=="SUB"):
	print(a-b-c-d)
elif(A=="MUL"):
	print(a*b*c*d)
elif(A=="DIV"):
	print(a/b/c/d)
else:
	print("wrong retered")
	