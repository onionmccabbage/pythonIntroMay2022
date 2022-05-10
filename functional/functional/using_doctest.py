# we can write simple tests within a module using 'doctest'
import doctest # import from the Python built-in library

def cube(x):
    ''' This function takes one numeric argument and returns the cube
    >>> cube(3)
    27
    >>> cube(-3) # docstring MUST use the three-chevrons >>> 
    -27
    '''
    return x**3

if __name__ == '__main__':
    # print( cube(3) ) # 27
    doctest.testmod(verbose=True) # here we invoke 'doctest' to run any tests written in the docstring