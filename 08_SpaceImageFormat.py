#!/usr/bin/env python3

"""
PART 1:
"""

S_W = 25
S_T = 6
lsiz = S_W*S_T

rwdat = open("data/08_input").readline()
pdig = [int(x) for x in rwdat]

# split the array in lsiz chunks (layers)
layers = [ pdig[i:i+lsiz] for i in range(0, len(pdig), lsiz) ]

# get all the nubmer of zeros and no.1*no.2 for all the layers
checkvals = [(x.count(0),(x.count(2)*x.count(1))) for x in layers if x.count(0) != 0]

# the layer with min. zeroes = checksum value
print("Checksum is:", min(checkvals, key=lambda x: x[0])[1])

"""
PART 2:
"""
# Render the layers from back to front and overwrite the pixels

TRANSPARENT = 2
BLACK = 0
WHITE = 1
finimg = [0]*lsiz
for l in reversed(layers):
    for p in range(len(l)):
        if l[p] == TRANSPARENT:
            continue
        elif l[p] == WHITE or l[p] == BLACK:
            finimg[p] = l[p]

# print the final image with colors
for s in range(lsiz):
    letter = '\33[100m' + " " + '\033[0m' if finimg[s] == 1 else '\33[107m' + " " + '\033[0m'
    print(letter, end="")
    if (s+1)%S_W == 0:
        print()


