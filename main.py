# by convention we often call our main module 'main'
# then we can import from other modules
# import basics2 # this will run all the immediate code in the imported module

# we use modules and imports to 'namespace' our code
import util # we aim to use the ' if __name__ == "__main__" ' check in modules

# we try to avoid polluting the global namespace
g = 'this is in the global namespace'
def main(): # by convention we often have a 'main' method
    k = 'local to this block scope'
    print(util.positiveCube(2)) # 8
    print(util.positiveCube(-2)) # 8
    # we can access global values
    global g # any reference to 'g' within this code block will actually acces the global 'g'
    print(g)
    g = 'access the global namespace' # this mutates the global 'g'
    print(g)

if __name__ == '__main__':
    main()
    print(g)