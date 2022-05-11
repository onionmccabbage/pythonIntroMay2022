# we can override ANY of the built-ins
# very commonly we override __str__ to change how print works

# here we override the equality operator
class Word(): # implicitly inherit from object
    '''
    this class compares word instancesregardless of case
    e.g. hello == Hello should be True
    '''
    def __init__(self, text):
        self.text = text # we could use get/set methods
    def __eq__(self, other_word): # __eq__ is the equality operator
        return self.text.lower() == other_word.text.lower()

# use with great care!!!!!!
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-than-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    word1 = Word('hello')
    word2 = Word('Hello')
    print( word1 == word2 ) #True!!!!