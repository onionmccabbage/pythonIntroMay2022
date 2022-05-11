class Todo(object): # explicitly inheerit from 'object'
    '''Here we declare a 'Todo' class
    property 'id' must be a positive integer
    property 'title' must be a non-empty string
    property 'completed' must be boolean
    '''
    def __init__(self, id, title, completed): # careful - the incoming parameters have the same name as the properties
        self.id = id
        self.title = title
        self.completed = completed
    # here is an alternative syntax for get/set methods (accessor and mutator methods)


if __name__ == '__main__':
    pass