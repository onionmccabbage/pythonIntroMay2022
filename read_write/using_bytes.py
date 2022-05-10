# as well as text files, we can work with byte files
# all files are ultimately bytes - .exe. dll, images, video, word/excel/ppt

def handleBytes(b): # receive incoming data - we should validate it
    # write the received bytes to a byte file
    fout = open('bfile', 'wb') # 'w' means (over)write 'b' means bytes
    fout.write(b) # we should be using try... except... here
    fout.close()

# read bytes back in
def readBytes():
    fin = open('bfile', 'rb')
    # fin = open('demo.xlsx', 'rb')
    r = fin.read()
    fin.close()
    print(r)


if __name__ == '__main__':
    # make some byte data
    b = bytes( range(0,256) ) # 0-255 are the first 256 characters
    # print(b) # looks odd, since bytes are not naturally human readable
    # pass the byte data to a file-writer
    handleBytes(b)
    readBytes()