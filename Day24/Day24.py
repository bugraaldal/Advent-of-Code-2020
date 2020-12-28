#This was... fun?
import numpy as np
with open("24.txt", "r") as f:
    _input = [each.strip() for each in f.readlines()]
# coords
placeChange = {"e": (2, 0), "se": (1, -1), "sw": (-1, -1), "w": (-2, 0),
               "nw": (-1, 1), "ne": (1, 1)}
directions = []
for k in _input:
    diectList = []
    ID = 0
    while ID < len(k):
        if k[ID] in ["e", "w"]:
            diectList.append(k[ID])
            ID += 1
        else:
            diectList.append(k[ID:ID+2])
            ID += 2
    directions.append(diectList)
tiles = {}
for direction in directions:
    position = [0, 0]
    for _dir in direction:
        change = placeChange[_dir]
        position[0] += change[0]
        position[1] += change[1]
    position_k = tuple(position)
    if position_k in tiles:
        tiles[position_k] = not tiles[position_k]
    else:
        tiles[position_k] = False
finalList = list(tiles.values())
print(f"Q1: {sum(~np.array(finalList))}")


def getNeighs(t):
    neighs = []
    for val in placeChange.values():
        neighs.append((t[0] + val[0], t[1] + val[1]))

    return neighs


# Black tiles
blacks = set([k for k, v in tiles.items() if not v])
for i in range(100):
    # neighbous
    neighs = {}
    for b in blacks:
        for n in getNeighs(b):
            if n in neighs:
                neighs[n] += 1
            else:
                neighs[n] = 1
    flip = set()
    for b in list(blacks):
        if not b in neighs or not neighs[b] in [1, 2]:
            blacks.remove(b)
            flip.add(b)
    whitexblack = set()
    for k in [k for k, v in neighs.items() if v == 2]:
        if k not in blacks and k not in flip:
            whitexblack.add(k)
    blacks = blacks.union(whitexblack)
    if i == 99:
        print(f"Q2: {len(blacks)}")
