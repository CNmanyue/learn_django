import urllib3
import json
import os
from urllib import request
from datetime import datetime

try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract

print('gjjcx go >>>')
img_url = 'http://app.szzfgjj.com:7001/pages/code.jsp'
img_dir = 'D:/pythonworkspace/gjjcx/verify/'
time = datetime.now().timestamp()*10000000
img_path_str = img_dir+time.__str__()+".png"
# 获取验证码图片
request.urlretrieve(img_url, img_path_str)
verify_str = pytesseract.image_to_string(Image.open(img_path_str))
print('验证码：',verify_str)

url_str = 'http://app.szzfgjj.com:7001/accountQuery?accnum=20780739155&certinum=431003199406012214&qryflag=1&verify='+verify_str
cookie = 'JSESSIONID=vyF6YNvNJ7DKCtNBpPLqGFy4BvS7FLq7FnHTmKHs82T1Gl92kbJK!868876301; path=/; domain=app.szzfgjj.com; HttpOnly'

http = urllib3.PoolManager()
r = http.request('GET',url_str)

print('result:',r.data.decode('utf-8'))
print('Set-Cookie:',r.headers.get('Set-Cookie'))
print('Content-Type:',r.headers.get('Content-Type'))