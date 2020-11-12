from sys import argv
import matplotlib.pyplot as plt
import struct

with open(argv[1], 'rb') as f: data = f.read()

signal = struct.unpack(f'{len(data)}b', data)

plt.plot(signal)
plt.axis('off')
plt.title('Recorded data')
plt.show()