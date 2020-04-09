import urllib.request
x = urllib.request.urlopen('https://pythonprogramming.net/urllib-tutorial-python-3/')
print(x.read())