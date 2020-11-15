from sys import argv

with open(argv[1], 'r') as f: data = f.read().split()

M = int(data[0])
elems = [int(e) for e in data[2:]]
N = len(elems)

values = dict()

def g (i, j):
    t = (i, j)
    if t not in values:
        if i == 0:
            values[t] = 0
        else:
            if j < elems[i-1]: values[t] = g(i-1,j)
            else: values[t] = max(g(i-1,j), g(i-1,j-elems[i-1]) + elems[i-1])
    
    return values[t]

print(g(N, M))