from sys import argv
from base64 import b64decode

with open(argv[1], 'r') as f: data = f.read()[7:]
data = b64decode(data)
with open(argv[2], 'wb') as f: f.write(data)