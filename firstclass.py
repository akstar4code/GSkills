import sys
def xsquare(y):
    return y*y
def xcube(x):
    return x**3
def my_map(func,lst):
    res = []
    for i in lst:
        res.append(func(i))
    return res
s = xsquare
c = xcube
squares = my_map(xsquare,[1,2,3,4,5,6])
cubes = my_map(xcube,[1,2,3,4,5,6])
print('squares',*squares)
print('cubes',*cubes)