#encrypting
def encry_tex(text,key):
    result=""
    for char in text:
        if char.isalnum():
            result=result+chr(ord(char)+key)
        else:
            result=result+char
    return  result
text=input("enter a text")
key=int(input("even a key"))
print(encry_tex(text,key))
