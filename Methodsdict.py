# dictionary methods
#get(key,"msg") msg is optional
d={"name":"student","age":33,"College":"guntur"}
value=d.get("name")
print (value)
value1=d.get("school")
#this value to print none because school key didn't there in d
print(value1)
value2=d.get("school ","key not found")
print(value2)
#update method
d1={"rno":34,"address":"Guntur","phone":9876543210}
d.update(d1)
print(d1)
#popitem()
#same as pop in the list and removing last to starting
d1.popitem()
print(d1)
#pop(key)
d1.pop("address")
print (d1)
#clear()
d1.clear()
print (d1
