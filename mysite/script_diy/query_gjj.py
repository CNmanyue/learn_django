# query_gjj.py

'''
	1. 使用requests，设置sessionid
	2. 使用了验证码识别技术（pytesseract,PIL,tesseract-ocr)
    pytesseract: https://github.com/madmaze/pytesseract
    tesseract-ocr: https://github.com/UB-Mannheim/tesseract/wiki
	params:
	argv[1] = 公积金帐号
	argv[2] = 身份证号码
'''

import os
import requests
# from datetime import datetime
import uuid
from PIL import Image
from io import BytesIO
import pytesseract
import sys


print("startup query_gjj ...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR：', BASE_DIR)

verify_code_dir = os.path.join(BASE_DIR, 'verify')
# time = datetime.now().timestamp() * 10000000
verify_code_path = os.path.join(verify_code_dir, uuid.uuid1().hex + '.png')
print("验证码图片路径：", verify_code_path)

verify_code_url = 'http://app.szzfgjj.com:7001/pages/code.jsp'
r_verify_code = requests.get(verify_code_url)
with open(verify_code_path, "wb") as f:
    f.write(r_verify_code.content)
verify_code_img = Image.open(BytesIO(r_verify_code.content))
verify_code_cookie = r_verify_code.cookies['JSESSIONID']
verify_code_num = pytesseract.image_to_string(verify_code_img)
print("验证码：", verify_code_num)


if len(sys.argv) < 3:
    accnum = '20780739155'
    certinum = '431003199406012214'
else:
    print('您输入的参数是：', sys.argv[1:])
    accnum = sys.argv[1]
    certinum = sys.argv[2]


# query_url = 'http://app.szzfgjj.com:7001/accountQuery?' +
# 'accnum=' + accnum + '&certinum=' + certinum + '&qryflag=1&verify=' + verify_code_num
# r = requests.get(query_url, cookies=dict(JSESSIONID=verify_code_cookie))

query_url = 'http://app.szzfgjj.com:7001/accountQuery'
payload = {'accnum': accnum, 'certinum': certinum, 'qryflag': 1, 'verify': verify_code_num}
r = requests.post(query_url, data=payload, cookies=dict(JSESSIONID=verify_code_cookie))
print("结果：", r.content.decode('utf-8'))
