def Fun1():
    print "In function 1"
    return "abc"

f1=Fun1()
f2 =Fun1
print "1 ",f1
print "2 ",f2
print type(Fun1)
print type(f1)
print type(f2)
f2()
print type(f2)
print type(f2())
# depending on the return type the type() is defined for a function