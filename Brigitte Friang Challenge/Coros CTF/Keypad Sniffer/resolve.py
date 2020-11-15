f = open("./output.txt", "r")
lines = f.read().split("\n")[:-1]

'''
Here we define a basic keypad mapping that will be coupled with the keypadsetup to get the code.
'''

keypadBaseMapping = [
    "01110111", #Top left of the keypad
    "10110111", #Top middle-left of the keypad
    "11010111", #Top middle-right of the keypad
    "11100111", #Top right of the keypad
    "01111011", #etc...
    "10111011", #....
    "11011011", #....
    "11101011", #....
    "01111101", #....
    "10111101", #....
    "11011101", #....
    "11101101", #....
    "01111110", #Bottom left of the keypad
    "10111110", #Bottom middle-left of the keypad
    "11011110", #Bottom middle-right of the keypad
    "11101110"  #Bottom right of the keypad
]

'''
Here we define the basic keypad setup based on the pics that we have.
'''

keypad = [
    "123F",
    "456E",
    "789D",
    "A0BC"
]

def keypadMapping(keypadSetup):
    out = dict()
    for i in range(4):
        for j in range(4):
            key = keypadBaseMapping[4*i+j]
            val = keypadSetup[i][j]
            out[key] = val

    return out

#Return input keypadsetup with a -90°C rotation
def rot(keypadSetup):
    new_keypad = [None]*4
    for i in range(4):
        txt = "".join([keypadSetup[j][i] for j in range(4)])
        new_keypad[3-i] = txt
    return new_keypad

# Return symetric of the input keypadsetup
def sym(keypadSetup):
    return [t[::-1] for t in keypadSetup]

# Calculate the code
def printCode(keypad):

    keypad_map = keypadMapping(keypad)

    grp = []
    tmp = []
    old = 0

    for line in lines:
        cur = line[4:].index("0")
        if cur == 0 and old == 3:
            grp.append(tmp)
            tmp = []
        tmp.append(line)
        old = cur

    input = []

    for group in grp:
        tmp = []
        for scan in group:
            tmp.append(keypad_map.get(scan, ""))
        tmp_set = set(tmp)
        tmp_set.remove("")
        if(len(tmp_set) == 0):
            input.append("rien")
        elif(len(tmp_set) == 1):
            input.append(tmp_set.pop())

    _input = [input[0]]
    for c in input:
        if c != _input[-1]:
            _input.append(c)

    print("DGSESIEE{"+"".join([c for c in _input if c != "rien"])+"}")

#Now, let's calculate and print the 8 possibilities

printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
keypad = rot(keypad)

keypad = sym(keypad)
printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
keypad = rot(keypad)
printCode(keypad)
