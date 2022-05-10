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
        # fout   = open('mylog.txt', 'w') # 'w' will (over)write 'a' will append - text is the default
        fout   = open('mylog.txt', 'x') # 'x' means exclusive access - only works if the file does NOT already exist
        size   = len(t)
        offset = 0
        chunk  = 24
        # we can loop over our text, writing a chunk at a time
        while True:
            if offset > size:
                fout.write('\n') # finish up with a new line character
                break # all done - nothing left to write
            else:
                fout.write(t[offset:offset+chunk]) # write a chunk of text
                offset += chunk # move the offset for the next iteration
    except FileExistsError as fe:
        print('The file cannot be written because it already exists {}'.format(fe))
    except Exception as e:
        print('Problem: {}'.format(e))
    finally:
        fout.close()
        print('all done')

# reading files elegantly
def fileReader():
    try:
        with open('mylog.txt', 'r') as fin: # 'r' will read (default is text)
            retrieved = fin.read()
            print(retrieved)
    except Exception as e:
        print(e)
    # NB using the 'with' operator will automatically close the file access object


if __name__ == '__main__':
    # simpleOutput()
    # simpleInput()
    # fileWriter('Lets hope this code works as intended - writing some output to a log')
    fileReader()