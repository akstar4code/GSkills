import requests
payload = {'username':'ashok','password':'testing'}
req = requests.get('https://httpbin.org/delay/1',timeout =3 )
print(req.text)
print(req)
#with open('comic.jpg','wb') as f:
#    f.write(req.content)