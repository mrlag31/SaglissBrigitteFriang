from sys import argv

with open(argv[1], 'r') as f: data = f.read().split()

M = int(data[0])
elems = [int(e) for e in data[2:]]
N = len(elems)

def g (i, j):
    if i == 0:
        return 0
    else:
        if j < elems[i-1]: return g(i-1,j)
        else: return max(g(i-1,j), g(i-1,j-elems[i-1]) + elems[i-1])

print(g(N, M))