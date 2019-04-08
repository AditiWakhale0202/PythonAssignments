class First():
    #print "we are in class one"

    def __init__(self, sum):
        self.num=5
        self.sum=sum
        print "num ",self.num
        print "sum ",self.sum

    class Inside():
        print "We are in class two"


obj1=First(15)
obj2=First.Inside()


