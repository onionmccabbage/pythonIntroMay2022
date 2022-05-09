def main(v):
    '''Validate the provided value to ensure it is alphabetic or numeric'''
    # check if the provided value is an alphabetic value
    if (v.isalpha()): # contains ONLY alphabetic characters
        return 'Alphabetic value is {}'.format(v)
    elif (v.isdecimal()): # contains ONLY numeric characters (no . or - etc)
        return 'Decimal value is {}'.format(v)

    else:
        return 'Non-alphanumeric value is {}'.format(v)

if __name__ == '__main__':
    q = input('enter something ') # this will be a string
    result = main(q)
    print(result)