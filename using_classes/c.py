# as an alternative we can use property 'decorators' (python 3 only)

class Todo(object): # explicitly inheerit from 'object'
    '''Here we declare a 'Todo' class
    property 'id' must be a positive integer
    property 'title' must be a non-empty string
    property 'completed' must be boolean
    '''
    def __init__(self, id, title, completed): # careful - the incoming parameters have the same name as the properties
        self.id = id # we actually end up calling the id setter method
        self.title = title # the methods names MUST match the property name
        self.completed = completed
    # here is an alternative syntax for get/set methods (accessor and mutator methods)
    @property # the '@' is 'decorator' syntax
    def id(self):
        return self.__id
    @id.setter # if we leave the setter out, we have a read-only property
    def id(self, id):
        if int(float(id))>0:
            self.__id = id # the double-underscore 'mangles' the property name (prevents direct access)
        else:
            self.__id = 1 # choose a sensible default
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        if type(title)==str and len(title)>0:
            self.__title = title # here we set the (name-mangled) property
        else:
            self.__title = 'default'
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, completed):
        if type(completed) == bool:
            self.__completed = completed
        else:
            self.__completed = False  
    def __str__(self):
        return 'This TODO has id: {} title:{} and completed {}'.format(self.__id, self.__title, self.__completed)

if __name__ == '__main__':
    t1 = Todo(-1, 'write stuff', False)
    print(t1.id) # use the getter method to access the id
    print(t1)