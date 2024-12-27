#function as decorator
def display_decorator(display):
    def inner_display(name):
        if name=="java":
            print ("good afternoon ",name)
        elif  name=="python":
            print("good evening")
        elif name=="HTML":
            print ("good night ",name)
        else:
           print("good bye")
        display(name)
    return inner_display 
@display_decorator
def display (name):
    print ("good morning",name)
display("java")
display("python")
display("HTML")
display("css")
