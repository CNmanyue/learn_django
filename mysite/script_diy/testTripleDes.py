import pyDes


# pyDes.des(key, [mode], [IV], [pad], [padmode])
# pyDes.triple_des(key, [mode], [IV], [pad], [padmode])

# key     -> Bytes containing the encryption key. 8 bytes for DES, 16 or 24 bytes
# 	   for Triple DES
# mode    -> Optional argument for encryption type, can be either
# 	   pyDes.ECB (Electronic Code Book) or pyDes.CBC (Cypher Block Chaining)
# IV      -> Optional Initial Value bytes, must be supplied if using CBC mode.
# 	   Length must be 8 bytes.
# pad     -> Optional argument, set the pad character (PAD_NORMAL) to use during
# 	   all encrypt/decrpt operations done with this instance.
# padmode -> Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
# 	   to use during all encrypt/decrypt operations done with this instance.


key = 'frJ0gfKGc0ui6CQSYh3ZRamK'
data = 'my name is zhouxw'
k = pyDes.triple_des(key,pad=None,padmode=pyDes.PAD_PKCS5)
value = k.encrypt(data=bytes(data,'utf-8'))
print('value:',	 value)
print('value:', value.hex().upper())
redata = k.decrypt(value)
print('redata:', redata.decode())

hexvalue = '9332FCE3E3678A7181176DCF249AF5F5D2A4E763480C0BBC7F78C5DEEFB6B7AD'
value = k.decrypt(bytes.fromhex(hexvalue))
print('解密值：', value.decode())