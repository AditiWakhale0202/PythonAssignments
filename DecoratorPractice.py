def writeme(name):
    def writerHer():
        print 'I was here '
        return name
    return writerHer()

@writeme
def Client(myName):
    print "call me "+ myName


var = Client('Aditi')