# Extremely hard. 
import collections
import itertools

inp = open("Day20.txt").read()
tilesLines = inp.strip().split("\n\n")
tilesSides = {}
tiles = {}
for tilelines in tilesLines:
    lt = ""
    rt = ""
    name, lines = tilelines[5:].split(":\n")
    lines = lines.split()
    for line in lines:
        rt += line[-1]
        lt += line[0]

    tilesSides[name] = (lines[0], rt, lines[-1], lt)
    tiles[name] = lines

# Convert to binary


def toNumber(s):
    return int(s.replace("#", "1").replace(".", "0"), 2)


tilesnum = {}
for name, strs in tilesSides.items():
    tilesnum[name] = tuple(map(toNumber, strs))


def sideReverse(side):
    return int("".join(reversed(format(side, "010b"))), 2)


def _find(base):
    possibleBase = set()
    possibleBase.update(tilesnum[base])
    possibleBase.update(map(sideReverse, tilesnum[base]))
    possibleadjcnt = set()
    for name, sides in tilesnum.items():
        if name == base:
            continue
        possiblesides = set()
        possiblesides.update(sides)
        possiblesides.update(map(sideReverse, sides))
        if len(possibleBase.intersection(possiblesides)):
            possibleadjcnt.add(name)
    return possibleadjcnt


adjcnt = {}
for name, sides in tilesnum.items():
    adjcnt[name] = _find(name)

# All of them are right
corners = set()
sides = set()
for name in sorted(adjcnt.keys()):
    numadj = len(adjcnt[name])
    if numadj == 2:
        corners.add(name)
    elif numadj == 3:
        sides.add(name)

x = 1
for name in corners:
    x *= int(name)
print("Q1:", x)


def findSide(sideName, _opposite):
    sides = list(adjcnt[sideName] - {_opposite})
    if len(adjcnt[sides[0]]) != 4:
        return sides[0]
    else:
        return sides[1]


image = []
row = []
cur = list(corners)[0]
while True:
    row.append(cur)
    adj = adjcnt[cur]
    if len(adj) == 2 and len(row) == 1:
        nxt = list(adj)[0]
        cur = nxt
    elif len(adj) == 2 and len(row) > 1:
        break
    else:
        cur = findSide(cur, row[-2])
image.append(row)

# Left side
sideLenght = len(sides) // 4 + 2
cur = list(adjcnt[row[0]] - {row[1]})[0]
while True:
    image.append([cur])
    if len(adjcnt[cur]) == 2:
        break
    cur = findSide(cur, image[-2][0])

# fill the image
for r in range(1, sideLenght):
    for c in range(1, sideLenght):
        p = list(
            adjcnt[image[r][c-1]].intersection(adjcnt[image[r-1][c]]) - {image[r-1][c-1]})
        if len(p) != 1:
            raise Exception("%d %d %s" % (r, c, p))
        image[r].append(p[0])


def _rotate(tile):
    new_tile = []
    for k in range(len(tile[0])):
        row = ""
        for r in range(len(tile) - 1, -1, -1):
            row += tile[r][k]
        new_tile.append(row)
    return new_tile


def flip(tile):
    new_tile = []
    for row in tile:
        new_tile.append("".join(reversed(row)))
    return new_tile


def M(tile):
    for _ in range(4):
        yield tile
        tile = _rotate(tile)
    tile = flip(tile)
    for _ in range(4):
        yield tile
        tile = _rotate(tile)


TOP = 0
RT = 1
BOT = 2
LT = 3


def getSide(tile, side):
    if side == TOP:
        return tile[0]
    elif side == BOT:
        return tile[-1]
    elif side == RT:
        return "".join(r[-1] for r in tile)
    else:
        return "".join(r[0] for r in tile)


imagespositioned = []
for corner, bottom in itertools.product(
        M(tiles[image[0][0]]),
        M(tiles[image[1][0]])):
    if getSide(corner, BOT) == getSide(bottom, TOP):
        break

match = False
for right in M(tiles[image[0][1]]):
    if getSide(corner, RT) == getSide(right, LT):
        match = True
        break
if not match:
    corner = flip(corner)
    bottom = flip(bottom)
    assert getSide(corner, BOT) == getSide(bottom, TOP)
    for right in M(tiles[image[0][1]]):
        if getSide(corner, RT) == getSide(right, LT):
            match = True
            break
assert match

tiles[image[0][0]] = corner
tiles[image[0][1]] = right
tiles[image[1][0]] = bottom

# Left
for r in range(2, sideLenght):
    top = tiles[image[r-1][0]]
    for bottom in M(tiles[image[r][0]]):
        if getSide(top, BOT) == getSide(bottom, TOP):
            tiles[image[r][0]] = bottom

for r in range(sideLenght):
    for c in range(1, sideLenght):
        left = tiles[image[r][c-1]]
        for right in M(tiles[image[r][c]]):
            if getSide(left, RT) == getSide(right, LT):
                tiles[image[r][c]] = right
                break

fullimage = []
for r in range(sideLenght):
    for l in range(1, 9):
        fullimage.append("".join(tiles[tilenum][l][1:-1]
                                 for tilenum in image[r]))

# Count sea monsters.
MONSTER = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]


def hasmonster(monster, r, c):
    for mr, mrow in enumerate(monster):
        for mc, ch in enumerate(mrow):
            if ch == "#":
                if fullimage[r+mr][c+mc] != "#":
                    return False
    return True


for monster in M(MONSTER):
    cnt = 0
    for r in range(len(fullimage) - len(monster) + 1):
        for c in range(len(fullimage[0]) - len(monster[0]) + 1):
            if hasmonster(monster, r, c):
                cnt += 1
    if cnt != 0:
        totalpounds = sum(row.count("#") for row in fullimage)
        monsterpounds = sum(row.count("#") for row in monster)
        print("Q2:", totalpounds - (monsterpounds * cnt))
        break
