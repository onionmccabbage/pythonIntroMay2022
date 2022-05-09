# Python is written in modules (script file)
# simple data types
from tkinter import Y


a = 7 # here a refers to a number value
b = 3 # these are integer values

# printing (in python 2 we can write 'print a' but we tend to use 'print(a)')
c = 7/b
print(c, type(c), type(b)) # the result is a float data-type

print(7//3) # integer division
print(7%3) # remainder or modulo
print(7**2) # power of...

# boolean
d = False # NB capital letter False and True

# more complex data types
a = {'name':'Ethel', 'age':42} # this is a dictionary (dict)
# the string data-type is a collection of characters
a = 'python' # now a refers to a string data-value (strings are immutable)
# a[0] = 'P' # ERROR
# strings are indexed from zero
print(a) # we can print the string
print( a[0:6:2] ) # [start:stop-before:step]
print(a[::-1]) # step through the collection backwards
print(a[6:0:-2]) # start at the end, stop before the beginning and step backards 2 !!

print(a[0:6:1]) #exhausts the string
print(a[6:0:-1]) # will miss the p
print(a[6:-1        :-1]) # goes empty
print(a[6::-1]) # works

# we use index to work with items in ordinal collections
l = [a, b, c, d, 'literal', 32.1] # this is a list: an ordinal collection of mixed data types
print(l[::2])

# we can ask the user to enter values (it will always be a string)
q = input('Please enter something then press return ') # python 2 use 'raw_input()'

if type(q)==str: # the colon indicates we will write a block of code
    print('You entered a string') # indentation represents a block of python code
# when we stop indenting, that is the end of the code block

print(q, type(q))

# we can define function as follows:
def myFunction(x,y): # a block...
    total = x+y
    diff  = x-y
    pow   = x**y
    return [total, diff, pow]
# the end of a block (no more indentation)
coffee = myFunction(b, 2)
print(coffee)