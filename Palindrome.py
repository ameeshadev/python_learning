#To check the word is palindrome or not
def reverse_string(string):
    reverse=""
    for ch in string:
        reverse=ch+reverse
    return reverse
string=input ("Enter a string: ")
reverse=reverse_string(string)
if string==reverse:
    print ("palindrome ")
else:
    print("not palindrome")
