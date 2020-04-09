x = 'Global 10'
def test():
    global x
    x = 'Local 10'
    print(x)
test()
print(x)