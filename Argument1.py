#keyword arguments
def intrest (price,time,rate):
    return(price*time*rate)/100
intrest (1000,12,3)
intrest(price=5000,time=15,rate=2.5)
print (intrest)
#variable length
def addition (*vargs):
    total=0
    for x in vargs:
        total+=x
    print ("sum=",total)
addition (1,2,3,4,5)
addition (10,20)
addition (1,2,3,4,5,6,7,8,9,10)
#output is 15,30 and 5
