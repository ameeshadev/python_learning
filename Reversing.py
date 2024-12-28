#reversing string
def reverse(string):
    result=""
    for word in string.split():
        reverse=""
        for ch in word:
            reverse=ch+reverse
        result=result+""+reverse
        result result
string=input("enter a string")
print(reverse(string))
