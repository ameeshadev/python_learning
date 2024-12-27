def my_generator():
    yield "java"
    yield "python"
    yield "dsa"
    yield "AI & ML"
    yield "fsd"
obj=my_generator()
print (next(obj))
print (next(obj))
print (next(obj))
for value in obj:
    print (value)
