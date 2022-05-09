def positiveCube(x):
    '''return the positive value of the cube of x'''
    c = x*x*x
    if (c<0):
        return c*-1
    else:
        return c

if __name__ == '__main__': # only run the following code if this is the MAIN mofule being run
    # exercise the module code
    print( positiveCube(3) ) # 27
    print( positiveCube(-3) ) # 27