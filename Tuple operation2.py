# tuple with different datatypes
t = ("immutable", True, 23)
print(t)
# Code for converting a list and a string into a tuple
a = [0, 1, 2]
t = tuple(a)
print(t)
# python code for creating tuples in a loop
t = ('gfg',)

# Number of time loop runs
n = 5 
for i in range(int(n)):
    t = (t,)
    print(t)
# Creating a tuple without brackets
t = 4, 5, 6
print(t)  # Output: (4, 5, 6)
