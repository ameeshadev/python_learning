#function as an arguments
def string_lower(string):
    return string.lower()
def string_upper(string):
    return string.upper()
def display_string(string, function):
    print (function (string))
s="AbCdEfGhij"
display_string(s, string_lower)
display_string(s, string_upper)
