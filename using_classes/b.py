# we can inherit from one class into another class
# here we will define a 'Coder' class
# a 'Coder' is also a 'Person'
from a import Person

# our 'Coder' class inherits everything from the 'Person' class
class Coder(Person):
    '''the Coder class extends the Person class
    to add a 'language' property'''
    def __init__(self, n, a, l):
        super().__init__(n, a) # call the parent
        self.__language = l
    def getLanguage(self):
        return self.__language
    # we can leave 'language' as read-only
    language = property(getLanguage)

    # we can overide the __str__ method
    def __str__(self):
        return 'This coder is {} aged {} writing {}'.format(self.name, self.age, self.__language)

if __name__ == '__main__':
    c = Coder('Ethel', 23, 'Python')
    print(c) # any time wwe try to print an instance of our Coder class, it will use __str__ method
    z = c.language
    print(z) # BUT if we try to access a property, the built-in __str__ is still used (default printout)
    # we can still access the original location of the classes
    pers = Person('Greta', 20)
    print(pers.__class__) # it was imported