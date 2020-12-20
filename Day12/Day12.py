""" Once again, I'm really happy with how this turned out to be. """
#from os import chdir
#chdir("/home/buura/Desktop/Python/AdventOfCode2020")
import re
data = []

with open("Day12.txt", "r") as f:
    matches = re.findall("([A-Z])([0-9]*)", f.read())
    data = [(m[0], int(m[1])) for m in matches]

dircts = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dirctName = ["E", "S", "W", "N"]
rotations = [-1, 1]
rotName = ["L", "R"]

# Part 1
def go(position, current_dirct, hndl, val):
    if hndl in dirctName:
        next_dirct = dircts[dirctName.index(hndl)]
        next_pos = (position[0] + next_dirct[0] * val,
                    position[1] + next_dirct[1] * val)
        return next_pos, current_dirct
    if hndl in rotName:
        i = dircts.index(current_dirct)
        n = int(val / 90)
        next_dirct = dircts[(
            i + rotations[rotName.index(hndl)] * n) % len(dircts)]
        return position, next_dirct
    elif hndl == "F":
        next_pos = (position[0] + current_dirct[0] *
                    val, position[1] + current_dirct[1] * val)
        return next_pos, current_dirct
    raise ValueError


position = (0, 0)
dirct = (0, 1)

for inst in data:
    position, dirct = go(position, dirct, inst[0], inst[1])

print(abs(position[0]) + abs(position[1]))

# Part 2

rot_mat = {"L": [[0, 1], [-1, 0]], "R": [[0, -1], [1, 0]]}


def rotate(mat, vec):
    v_0 = vec[0] * mat[0][0] + vec[1] * mat[0][1]
    v_1 = vec[0] * mat[1][0] + vec[1] * mat[1][1]
    return (v_0, v_1)


def go_w(goPosition, position, hndl, val):
    if hndl in dirctName:
        next_dirct = dircts[dirctName.index(hndl)]
        goPosition = (goPosition[0] + next_dirct[0]
                      * val, goPosition[1] + next_dirct[1] * val)
        return goPosition, position
    if hndl in rotName:
        d_x = goPosition[1] - position[1]
        d_y = goPosition[0] - position[0]
        rel_pos = (d_y, d_x)
        mat = rot_mat[hndl]
        n = int(val / 90)
        rotated = rotate(mat, rel_pos)
        for i in range(n - 1):
            rotated = rotate(mat, rotated)
        goPosition = (position[0] + rotated[0],
                      position[1] + rotated[1])
        return goPosition, position
    elif hndl == "F":
        n_0 = goPosition[0] - position[0]
        n_1 = goPosition[1] - position[1]
        next_pos = (position[0] + val * n_0, position[1] + val * n_1)
        goPosition = (goPosition[0] + val *
                      n_0, goPosition[1] + val * n_1)
        return goPosition, next_pos


position = (0, 0)
go = (1, 10)

for inst in data:
    go, position = go_w(go, position, inst[0], inst[1])

print(abs(position[0]) + abs(position[1]))

vec = (0, 10)
mat = rot_mat
