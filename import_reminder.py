from reminder import main as r
def main():
    r()
    print('The main module is being named {}'.format(__name__) )


if __name__ == '__main__':
    main() # run THIS module's main function