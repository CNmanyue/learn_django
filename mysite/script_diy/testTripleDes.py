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

data = "1234567890"

k = pyDes.triple_des('zUy2Ag3mM9TLe3lm4oO0WK4J')
d = k.encrypt(data=data.encode('ascii'),pad=None,padmode=pyDes.PAD_PKCS5)
strd = d.hex().upper()
print('encrypted:',strd)


dd = k.decrypt(d)
strdd =dd.decode('utf-8')
print('decrypted:',strdd,'dd:',dd)

with open('tripleDesData.txt','w') as f:
	f.write(strdd)

