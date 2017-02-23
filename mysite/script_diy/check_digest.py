import hashlib
import base64
import pyDes

app_id = '200001'
app_secret = 'zUy2Ag3mM9TLe3lm4oO0WK4J'
timestr = '20170220101010'
idcard = '431003199106012212'
mobile = '18926460050'

md5 = hashlib.md5()
sha1 = hashlib.sha1()

md5.update(timestr.encode('utf-8'))
strmd5 = md5.hexdigest().upper()
print('md5:', strmd5)

sha1.update(app_secret.encode('utf-8'))
strsha1key = sha1.hexdigest().upper()
print('sha1key:', strsha1key)

_strtemp = app_id + strmd5 + strsha1key
print('_strtemp:', _strtemp)
sha1 = hashlib.sha1()
sha1.update(_strtemp.encode('utf-8'))
strsha1 = sha1.hexdigest().upper()
print('sha1:', strsha1)

# print('bytes:',strsha1.encode('ISO-8859-1'))

strbase64 = base64.b64encode(strsha1.encode('ascii'))
print('base64:', strbase64)

strdecode = base64.b64decode(
    b'QjFGOTkyQkY0RDE5QUQyNjc1RTRBM0JFMURCM0NCRjREQkY1NTQyOA==')
print('strdecode:', strdecode)

import requests as reqs
msg_digest = strbase64.decode('ascii')
print('msg_digest:', strbase64.decode('ascii'))
k = pyDes.triple_des(app_secret)
d = k.encrypt(data=(idcard + '|' + mobile).encode('ascii'),
              pad=None, padmode=pyDes.PAD_PKCS5)
id_mobile = d.hex().upper()
canshu = {'app_id': app_id, 'timestamp': timestr, 'msg_digest': msg_digest,
          'customer_name': 'zhouxw', 'id_mobile': id_mobile,
          'email': 'z201702211@fdd.com'}
print('req data:', canshu)
r = reqs.post('http://10.51.0.165:8888/api/syncPerson_auto.api', params=canshu)
print("response:", r.text)
print("r.content:", r.content.decode('utf-8'))
