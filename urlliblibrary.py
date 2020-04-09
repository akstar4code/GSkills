import urllib.request
import urllib.parse
#x = urllib.request.urlopen('https://pythonprogramming.net/urllib-tutorial-python-3/')
#print(x.read())
url = 'https://pythonprogramming.net/search/'
values = {'q':'plot'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)