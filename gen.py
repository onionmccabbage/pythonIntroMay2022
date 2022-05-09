# here we will explore range, generator and comprehension
def demo(begin, end, step):
    # types of generator: list, tuple etc.
    num_g = (num for num in range(begin, end, step) if num >0) # [] would make a list generator
    print(type(num_g))
    for _ in num_g:
        print(_)

# other types of comprehension
def demo2():
    p = 'are we there yet'
    # here is an example of dictionary comprehension - we comprehensively deal with each member
    characters = {letter:p.count(letter) for letter in p}
    print (characters)

def customGen(): # we can write our own custom generator
    '''Generate a sequence of square numbers'''
    number = 0
    while number < 11:
        number += 1
        yield number**2 # yield the square of each number

def normalFunction():
    return 'normal functions can return ONE thing'

if __name__ == '__main__':
    demo(-999, 30, 3)
    demo2()
    # use our custom generator
    gen = customGen() # we now have an instance of our generator
    print(type(gen)) # it is a generator because it has a 'yield' statement
    print( gen.__next__() )  # the square of 1
    print( gen.__next__() )  # the square of 2
    print( gen.__next__() )  # the square of 3
    for _ in gen:
        print(_) # yield all the remaining values from our custom generator instance