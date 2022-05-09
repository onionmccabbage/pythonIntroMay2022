# ranges, iterables etc.
def main():
    pass # pass is handy as a placeholder - code you will fill in later
    i = 99
    while i != 0: # or > < >= <=
        print(i)
        i-=1 # same as i=i-1
        if i<98:
            break # break out of the loop # quit would stop the current block

if __name__ == '__main__': # all immediate code should be here
    main()
    # range (and generators)
    r = range(10,-10,-1)
    print(type(r))
    # we can use the range to populate a list - in memory
    num_l  = [num for num in r] # range uses start, stop-before, step
    print (num_l, type(num_l))

    # the generator type
    num_g = (i for i in r) # the roundbrackets make a generator
    print(type(num_g))
    # a generator can 'yield' values
    print( num_g.__next__() ) # __next__ is a generator method to yield the next value in the sequence
    print( num_g.__next__() )
    print( num_g.__next__() )
    print( num_g.__next__() )
    print( num_g.__next__() )
    print( num_g.__next__() )
    print('----')
    # we can use conventional looping to iterate and yield the next values of a generator
    for item in num_g:
        print(item)
    # at this point, the generator has been exhausted - there are no further values to yield
    print('----')
    # print( num_g.__next__() ) # nothing left to yield!! we get an exception

    # using range, generators and 'comprehension'
    odd_t = (num for num in r if num%2 == 1) # this returns lots of ODD numbers
    even_l = [num for num in r if num%2 == 0] # ...even numbers in range
    print(-7 in even_l) # False
    
# casting user input. Maybe we need an integer from the user
i = input('Enter an integer ')
# cast the entered string to an int
i_int = int(float(i)) # cast to a float then cast to an int
print(i, type(i), i_int, type(i_int))
