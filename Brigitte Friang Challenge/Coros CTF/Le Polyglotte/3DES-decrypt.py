from sys import argv
import pyDes as des

key = b'\xce]`^+5w#\x96\xbbsa\x14\xa7\x0ei'
iv = b'\xc4\xa7\x1e\xa6\xc7\xe0\xfc\x82'
with open(argv[1], 'rb') as f: data = f.read()

alg = des.triple_des(key, des.CBC, iv)
out = alg.decrypt(data)

with open(argv[2], 'wb') as f: f.write(out)