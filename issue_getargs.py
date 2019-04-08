def a_function(var1,var2, var3):
    variables= var1,var2,var3
    print variables
    a_list = list(variables)
    print a_list
    for l in a_list:
        if l is None:
            a_list[a_list.index(l)] = ''
    variables = tuple(a_list)
    print a_list
    print var1+var2+var3


a_function('a','kindle','pic')
a_function(None,'needle','no')
#a_function('ball',None,None)

