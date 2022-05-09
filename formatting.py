def main():
    words = 'nearly tea time'
    w_l = list(words)
    print(w_l)
    # convert the list back to a string
    w = ''.join(w_l)
    print(w)
    # print formatting
    a = 9
    b = True
    c = ('tea', 'coffee', 'water')
    # we can inject any data members into a string using their order
    print( 'Time for {} {} or {}'.format(c[0], c[1], c[2])   )
    print( 'Time for {2} {0} or {1} - I\'ll have some {0}'.format(c[0], c[1], c[2])   )

if __name__ == '__main__':
    main()