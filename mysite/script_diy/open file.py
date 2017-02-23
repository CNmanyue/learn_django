import requests

r = request.post('https://m.youjizz.com/page100.html')

f = open(r'xx.html',w)
f.write(r.text)
