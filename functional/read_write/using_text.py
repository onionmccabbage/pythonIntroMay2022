# we can write to text files and retrieve back from text files
def simpleOutput():
    '''Python uses file access objects
    If a file access object points to a non-existant file, it will create the file
    We can choose to append, overwrite or exclusive access a file via a file acces object
    '''
    # we need a file access object
    fout = open('output.txt', 'at') # 'a' means append 't' means 'text'
    # we can choose ot redirect print output tot a file access object
    print('here is some content', file=fout)
    fout.close() #always a god iodea to tidy up!

def simpleInput():
    '''we can use file access object to read from a text file'''
    try:
        filename = 'output.txt'
        fin = open(filename, 'rt') # 'r' means read 't' means text
        received = fin.read() # read the entire file
        print(received)
    except Exception as e:
        print('Problem with access to {} {}'.format(filename, e))
    finally:
        if (fin):
            fin.close() # always close the resource

def fileWriter(t): # we expect some input
    '''write text to a file in chunks - progressively'''
    try:
        fout   = open('mylog.txt', 'a') # 'a' will append - text is the default
        size   = len(t)
        offset = 0
        chunk  = 24
        # we can loop over our txt, writing a chunk at a time
        while True:
            if offset > size:
                fout.write('\n') # finish up with a new line character
                break # all done - nothing left to write
            else:
                fout.write(t[offset:offset+chunk]) # write a chunk of text
                offset += chunk # move the offset for the next iteration
    except Exception as e:
        print('Problem: {}'.format(e))
    finally:
        fout.close()
        print('all done')

if __name__ == '__main__':
    # simpleOutput()
    # simpleInput()
    fileWriter('it is nearly time for lunch so lets hope this code works as intended')