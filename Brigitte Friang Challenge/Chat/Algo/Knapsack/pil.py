from sys import argv

with open(argv[1], 'r') as f: data = f.read().split()

M = int(data[0])
elems = [int(e) for e in data[2:]]
N = len(elems)

values = dict()

pile = [ (N, M) ]
while pile != []:
    i, j = t = pile.pop()
    if t in values: continue
    
    if i == 0:
        values[t] = 0
    else:
        t0, t1 = (i-1,j), (i-1,j-elems[i-1])
        u, v = t0 not in values, t1 not in values
        if u or v:
            pile.append(t)
            pile.append(t0)
            pile.append(t1)
            continue
        elif j < elems[i-1]:
            values[t] = values[t0]
            continue
        else:
            values[t] = max(values[t0], values[t1] + elems[i-1])
            continue

print(values[ (N, M) ])