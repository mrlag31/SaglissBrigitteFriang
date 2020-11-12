from sys import argv

with open('intercepte.txt', 'rb') as f: intercepte = f.read()
with open('original.txt', 'rb') as f: original = f.read()

index_i = 0
index_o = 0
res = bytes()

while index_i < len(intercepte) and index_o < len(original):
    while intercepte[index_i] != original[index_o]:
        res += bytes([intercepte[index_i]])
        index_i += 1
    index_o += 1
    index_i += 1
    
res += intercepte[index_i:]
with open(argv[1], 'wb') as f: f.write(res)