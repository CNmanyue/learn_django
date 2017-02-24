#!/usr/bin/env python

'''
1. 查询公积金情况
2. 使用了验证码识别技术（pytesseract,PIL,tesseract-ocr)
    pytesseract: https://github.com/madmaze/pytesseract
    tesseract-ocr: https://github.com/UB-Mannheim/tesseract/wiki
3. 设置Cookie通过验证码
'''

import urllib3
# import json
import os
from datetime import datetime

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

print('gjjcx go >>>')
http = urllib3.PoolManager()

img_url = 'http://app.szzfgjj.com:7001/pages/code.jsp'
# <<<<<<< HEAD
# img_dir = 'D:/pythonworkspace/gjjcx/verify/'
# time = datetime.now().timestamp() * 10000000
# img_path_str = img_dir + time.__str__() + ".png"

# # 获取验证码图片
# r_img = http.request('GET', img_url)
# f_img = open(img_path_str, 'wb')
# f_img.write(r_img.data)
# f_img.close()
# =======
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('base_dir', BASE_DIR)
img_dir = BASE_DIR + '\\verify\\'
time = datetime.now().timestamp() * 10000000
img_path_str = img_dir + time.__str__() + ".png"

# 获取验证码图片
r_img = http.request('GET', img_url)
with open(img_path_str, 'wb') as f_img:
    f_img.write(r_img.data)
# f_img = open(img_path_str,'wb')
# f_img.write(r_img.data)
# f_img.close()

img_cookie = r_img.headers.get('Set-Cookie')
print('获取验证码Cookie:', img_cookie)

verify_str = pytesseract.image_to_string(Image.open(img_path_str))
print('验证码：', verify_str)

url_str = 'http://app.szzfgjj.com:7001/accountQuery?accnum=20780739155&certinum=431003199406012214&qryflag=1&verify=' + verify_str
print('查询URL:', url_str)

cookie = 'JSESSIONID=vyF6YNvNJ7DKCtNBpPLqGFy4BvS7FLq7FnHTmKHs82T1Gl92kbJK!868876301; path=/; domain=app.szzfgjj.com; HttpOnly'

r = http.request('GET', url_str, headers={"Cookie": img_cookie})
print('result:', r.data.decode('utf-8'))

print('提交查询的Cookie:', r.headers.get('Set-Cookie'))
print('提交查询的Cookie:', r.headers.get('Cookie'))
# print('[headers]\n',r.headers)
