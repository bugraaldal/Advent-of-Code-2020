# Part 2 is too slow. I might try to find a faster solution.
_input = []
rows = []
with open("Day17.txt", "r") as f:
    _all = f.read().rstrip().split(("\n"))
    for each in _all:
        rows.append(each)
    for row in rows:
        _input.append(row)


def cubes(grid, part2):
    active_cubes = set()
    _y = len(_input)
    _x = len(_input[0])

    for y in range(_y):
        for x in range(_x):
            if grid[y][x] == "#":
                if part2:
                    active_cubes.add((x, y, 0, 0))
                else:
                    active_cubes.add((x, y, 0))

    return active_cubes


def getNeighbor(coordinates):
    neighbours = []
    chances = [-1, 0, 1]
    for nx in chances:
        for ny in chances:
            for nz in chances:
                if len(coordinates) == 4:
                    x, y, z, w = coordinates
                    for nw in chances:
                        if nx != 0 or ny != 0 or nz != 0 or nw != 0:
                            neighbours.append((x+nx, y+ny, z+nz, w+nw))
                else:
                    x, y, z = coordinates
                    if nx != 0 or ny != 0 or nz != 0:
                        neighbours.append((x+nx, y+ny, z+nz))
    return neighbours


def count_neighbours(active_cubes, coordinates):
    cnt = 0
    for neighbour in getNeighbor(coordinates):
        if neighbour in active_cubes:
            cnt += 1
    return cnt


def execute(active_cubes):
    temp_active_cubes = set()

    for coordinates in active_cubes:
        if count_neighbours(active_cubes, coordinates) in [2, 3]:
            temp_active_cubes.add(coordinates)

        for n_coordinates in getNeighbor(coordinates):
            if n_coordinates not in active_cubes and count_neighbours(active_cubes, n_coordinates) == 3:
                temp_active_cubes.add(n_coordinates)

    return temp_active_cubes


def Part1():
    active_cubes = cubes(_input, False)
    for _ in range(6):
        active_cubes = execute(active_cubes)

    return len(active_cubes)


def Part2():
    active_cubes = cubes(_input, True)
    for _ in range(6):
        active_cubes = execute(active_cubes)

    return len(active_cubes)


print("Q1:", Part1())
print("Q2:", Part2())
