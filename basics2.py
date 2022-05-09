# quotes
j = "double\t \n  \" quotes"
k = 'single\t \n  \' quotes'
l = '''tripple quotes
new lines, tabs etc are 
    all preserved in tripple quotes'''
m = """tripple double quotes"""

def FnA():
    ''' we tend to use tripple quotes to write docstrings
    This lets us write some terse explanation about the function
    Often used to document a function'''

# more about lists - lists are mutable
l = [] 
l = list('make a list out of a string') # we cast the string as a list
l[0] = 'M'
l.append('!')
l.pop() # removes the last member
l.insert(5, False)
# print(l)

# we also have an IMUTABLE ordinal collection called a tuple
t = (8,7,6,5,l,'anything')
# t[0] = False #nope
t[4][2] = 'changed'

print(t[0:5])

# we can type case
q = (l,) # the comma indicates it will become a tuple. Or say tuple(l)
print(type(q))

# large numbers
g = 10**100000 # python is only restricted by system resources
print(g)