import timeit
modu = '''from math import pow'''
code2 = '''def fun():
    mylist = []
    for i in range(100):
        mylist.append(i**i)
    '''
code = '''def fun():
    mylist = []
    for i in range(100):
        mylist.append(pow(i,i))'''
print(timeit.timeit(stmt=code,setup=modu,number=1000000))
print(timeit.timeit(stmt=code2,number=1000000))
print(timeit.repeat(stmt=code2,number=1000000,repeat=3)) #

