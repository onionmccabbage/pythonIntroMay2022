# we can compose classes from other classes (and other structures)
# this is called composition

class Bill():
    def __init__(self, bill_desc):
        self.bill_desc = bill_desc

class Tail():
    def __init__(self, tail_desc):
        self.tail_desc = tail_desc

class Duck():
    '''
    The Duck class needs to be able to count how many instances are created
    '''
    count = 0 # this is a property of the class (accessible via any class instance)
    def __init__(self, bill, tail): # compose this duck by using the bill and tail classes
        self.bill = bill
        self.tail = tail
        Duck.count += 1 # every time a new instance is created, we increment the count
    @classmethod # a method call-able onthe CLASS (rather than on instances of the class)
    def numDucks(cls): # we do not pass 'self' but we must pas the actual class
        return 'There have been {} ducks created'.format(cls.count)
    def __str__(self):
        return 'This duck has a {} bill and a {} tail'.format(self.bill.bill_desc, self.tail.tail_desc)

if __name__ == '__main__':
    b = Bill('long orange')
    t = Tail('medium')
    d = Duck(b, t)
    howard = Duck(b, t)
    ella   = Duck(b, t)
    donald = Duck(b, t)
    # we call static methods on the class itself (or via any instance)
    n = Duck.numDucks()
    print(d, n)
    # we can access the docstring (if it exists)
    print(d.__doc__)
    print(d.__class__)
    print(d.__dict__)
