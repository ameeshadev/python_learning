from data import main_username,main_password
username=str(input("enter:_"))
password=str(input("enter:_"))

if (username==main_username):
	if (password==main_password):
		print("logind")
	else:
		print("wrong")
else:
	print("wrong password")
	