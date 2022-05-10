# here we will explore functional programming in Python
# by convention we use 'args'. it is the asterisk that collects the arguments together
def myArgs(*args): # we can choose to pass positional arguments to any python function
    # ALL arguments passed into a funtion will exist in the 'args' tuple
    print(type(args) ) #, args[0])
    # we can make our function operate differently based on the number of arguments
    if len(args)==0:
        # we have a no-args version of our function
        print('Function was called with no arguments')
    elif len(args)==1:
        print('Single positional arguemnt is {}'.format(args[0]))
    else:
        for _ in args:
            print('Positional argument {}'.format(_) )

def myKwargs( **kwargs ): # by convention we use 'kwargs' to collect the key-word arguments
    # any key-word arguments will be gathered into the 'kwargs' dictionary
    print(type(kwargs))
    for k, v in kwargs.items():
        print('{} contains {}'.format(k,v))

def both( *args, **kwargs ): # we can use both
    print( args, kwargs )

if __name__ == '__main__':
    myArgs(42, True, {}, (4,3,2)) # these are positional arguments
    myArgs([5,4,3])
    myArgs()
    # key-word arguemnts are set EQUAL to a value and comma separated
    myKwargs(x=3, y=4) # these are key-word arguments
    both()
    both(1,2,3,4) # args
    both(x=4, y=3) # kwargs
    both('a', True, other=[]) # args then kwargs