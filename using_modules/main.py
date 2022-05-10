# we can import our own modules
from sys_path import getInfo

def main():
    i = getInfo()
    print('Python is running on {} with a max object size of {}'.format(i['p'], i['max']))

if __name__ == '__main__':
    main()