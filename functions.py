method=str(input())
def add():
	a=int(input("enter a number:_"))
	b=int(input("enter a number:_"))
	return a+b

def sub():
	a=int(input("enter a number:_"))
	b=int(input("enter a number:_"))
	return a-b


def mul():
	a=int(input("enter a number:_"))
	b=int(input("enter a number:_"))
	return a*b	
	
def div():
	a=int(input("enter a number:_"))
	b=int(input("enter a number:_"))
	return a/b

if (method=="add"):
	print(add())
if (method=="sub"):
	print(sub())
if (method=="mul"):
	print(mul())
if (method=="div"):
	print(div())

