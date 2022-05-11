# we will write a 'Person' class, encpasulating name and age
# we could just use a structure
p = {'name':'Ada', 'age':120} # here we are actually using the 'Dict' class
p['age'] = -99
p['name'] = True # oh dear!!

# or we could write a person function
def Pers(n, a):
    if type(n)== str:
        p = {'name':n}
    return p

# NB in Python EVERYTHING is an object

# but if we need full control over the lifecycle of the entity, we need a class
class Person(): # by default all classes inherit from 'object'
    '''Explain your class with a docstring
    This class encapsulates a 'person' with 
    parameters for 'name' and 'age' (validated)'''
    def __init__(self, n, a): # __init__ is like a constructor
        self.__name = n # these are properties of this class
        self.__age  = a # the double underscore 'mangles' the '__age' property-name
    def setAge(self, new_age): # here we define methods of this class
        if int(float(new_age)) > 0 :
            self.__age = new_age
        else:
            self.__age = 42 # choose a sensible default
    def getAge(self):
        return self.__age
    def setName(self, new_name):
        if type(new_name)==str and len(new_name)>0: # or new_name != ''
            self.__name = new_name
        else:
            self.__name = 'Default'  
    def getName(self):
        return self.__name
    def __str__(self): # we override the built-in '__str__' method, which is used by 'print'
        return 'this person is {} aged {}'.format(self.name, self.age)
    age = property(getAge, setAge) # specify which methiods will get and set the age value
    name = property(getName, setName)

if __name__ == '__main__':
    # we can create instances of our class
    t = Person('Timnit', 38)
    a = Person('Ada', 120)

    # we can mutate properties of our instances
    # t.setAge(39)
    # we might prefer to write (context tells the class whether tot use get or set)
    # we have declared 'accessor' and 'mutator' methods (get/set)
    t.age = 39 # this looks like a property but actually it calles the 'setAge' method
    t.name=999 # we do not want direct access to properties of this class
    print( t.age, t.getName() )
    print( t ) # uses the __str__ method




