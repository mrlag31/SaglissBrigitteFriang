message = "Zp cvbz whyclulg h spyl jl tlzzhnl, j'lza xbl cvbz wvbclg"
low_A = ord('a')
upp_A = ord('A')

for i in range(26):
    decoded = ''
    for c in message:
        if not c.isalpha():
            decoded += c
        if c.islower():
            offset = (ord(c) - low_A + i) % 26
            decoded += chr(offset + low_A)
        if c.isupper():
            offset = (ord(c) - upp_A + i) % 26
            decoded += chr(offset + upp_A)

    print(f'+{i}\t- ' + decoded)