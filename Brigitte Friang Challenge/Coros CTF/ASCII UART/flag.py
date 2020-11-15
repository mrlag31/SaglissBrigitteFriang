from sys import argv
import struct

parity = argv[1] == 'True'
with open(argv[2], 'rb') as f: data = f.read()
UART_signal = struct.unpack(f'{len(data)}b', data)

def get_first_UART (bits, parity=False):
    max_len = 9 + parity
    start = 0
    while bits[start] == 1 and start + max_len < len(bits): start += 1
    if start + max_len >= len(bits):
        return
    
    data = bits[start+1:start+9]
    end = start + max_len
    pbit = pbit = bits[start+9] if parity else None
    correct = (bits[end] == 1) and parity_check(data, pbit)

    return start, data, pbit, correct, end

def parity_check (bits, parity):
    if parity == None: return True
    xor = 0
    for b in bits: xor ^= b
    return xor == parity

def read_UART (bits, parity=False):
    UART = (0,)
    cur = 0
    while UART:
        if UART: cur += UART[-1]
        UART = get_first_UART(bits[cur:], parity)
        if UART and not UART[-2]: continue

        yield UART

def compress_as_byte (bits):
    return sum([
        bits[i]*2**i for i in range(8)
    ])

out = [*read_UART(UART_signal, parity)][:-1]
ASCII = [chr(
    compress_as_byte(b[1])) for b in out
]

print(''.join(ASCII))