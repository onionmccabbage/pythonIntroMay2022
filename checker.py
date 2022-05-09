# import a module by it's name
import validate as v # everythnig in the module is available

# alternatively we can import just parts of a module
from validate import main as m

def main():
    print( v.main('hello') )
    print( m('hello') ) # use our imported function

if __name__ == '__main__':
    main()