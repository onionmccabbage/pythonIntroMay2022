import sys # sys represents the system on which Python is running

def getInfo():
    info = {'p':sys.platform, 'path':sys.path, 'max':sys.maxsize}
    return info

if __name__ == '__main__':
    print( getInfo() )