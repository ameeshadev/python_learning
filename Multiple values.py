#a python return multiple values
#return multiple values
def sample (a,b):
    sum=(a+b)
    sub=(a-b)
    mul=(a*b)
    div=(a/b)
    return sum,sub,mul,div
a,b=map(int,input("Enter 2 values: ").split())
a1,a2,a3,a4=sample(a,b)
print(f"sum={a1}\n  diff={a2}")
print (f"mul={a3}\n div={a4}")
