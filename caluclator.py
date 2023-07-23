method=str(input())
num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
num3=int(input("enter a number3"))
def calu(num1,num2,num3,method):
	if (method=="add"):
	   return num1+num2+num3
	if (method=="sub"):
	   return num1-num2-num3
	if (method=="mul"):
	   return num1*num2*num3
	if (method=="div"):
	   return num1/num2/num3
	
print(calu(num1,num2,num3,method))