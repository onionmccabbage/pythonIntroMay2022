# more on dictionaries and nesting collections

def main():
    # dictionaries are NOT ordinal, they have NO numeric sequence of members
    d1 = {'name':'Timnit', 'age':42, 'member':True }
    d2 = {'name':'Grace',  'age':82, 'member':True}
    d3 = {'name':'Ada',    'age':142, 'member':False}
    # we can add arbitrary members to our dictionaries
    d2['wibble'] = True
    # a dict is really useful to ensure unique keys for values
    members_d = {'a':d1, 'b':d2, 'c':d3}
    # the members of our data collection remain mutable
    # print(members_d['a']['age'])
    members_d['a']['age'] = 43
    d2['age'] = 83
    print(d2.keys(), d2.values())
    # even though dict is NOT indexed by number, we can still iterate over it's items
    for (key, value) in d2.items():
        print(key, value)

    # Python has a 'None' type
    n = None # not the same as undefined

    # ways to create structures
    w = dict() # empty dictionary
    x = list( (4,3,2) ) # make a list out of a tuple
    x = [ (4,3,2) ] # same again
    y = tuple(x) # make a tuple out of a list
    y = (x,) # again, make a tuple this time containing one member (our list)

    # there is also a data-type called a set
    s = {7,6,5,5,3,7,1,9} # the members of a set are unique
    s.add(0)
    print(s)

if __name__ == '__main__':
    main()