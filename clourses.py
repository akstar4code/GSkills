'''def outer_fun():
    msg = 'Hello'
    def inner_fun(name):
        print(msg,name)
    return inner_fun
my_fun = outer_fun()
my_fun(input())
'''
## Decorators
def decorator_fun(original_fun):
    def wrapper_fun(*args,**kwargs):
        print('Before the functions :',original_fun.__name__)
        return original_fun(*args,**kwargs)
    return wrapper_fun
@decorator_fun
def display():
    print('Hello')
@decorator_fun
def display_info(name,age):
    print('Name:',name,'\nAge:',age)

display()
display_info('Ashok',21)
