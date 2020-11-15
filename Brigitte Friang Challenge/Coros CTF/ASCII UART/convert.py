from sys import argv
import struct

with open(argv[1], 'rb') as f: data = f.read()

signal = struct.unpack(f'{len(data)}b', data)
signal = [1 if b>0 else 0 for b in signal]

counts = []
counter = 0
cur = 1
for b in signal:
    if b == cur: counter += 1
    else:
        counts.append(counter)
        cur = b
        counter = 0

fs = min(counts) # Sampling frequency
start = fs//2

UART_signal = bytes(signal[start::fs])

with open(argv[2], 'wb') as f: f.write(UART_signal)