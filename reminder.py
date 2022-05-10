from re import A


def main():
    # using 'in'
    t = ('posts', 'albums', 'todos', 'photos') # a tuple (immutable)
    exists = 'users' in t # False (its not in the tuple)
    print(exists)
    # iterating over a dict
    d = {'name':'Grace Hopper', 'admin':False, 'address':[42, 'Primrose Av', 'Becknall']}
    for k, v in d.items():
        if(type(v)==list):
            for item in d[k]:
                print('\t{}'.format(item))
        else:
            print('Key {} has value {}'.format(k, v))
    # passing by ref or passing by value
    e = d # we now have two identifiers pointing to the SAME memory location
    d['admin'] = True
    print(e['admin']) # we access by REFERENCE to the same structure
    # but for simple variables...
    a = 42
    b = a # pass by VALUE (not by reference)
    a = 24
    print(b)
    # so just what is __name__?
    print('This module is being named {}'.format(__name__) ) # Python will ALWAYS assign a __name__ to every module being executed

if __name__ == '__main__':
    main()
    # import this