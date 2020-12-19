with open("Day3.txt", "r") as f:
    input = f.read().split("\n")


def Route(X, Y, grid):
    trees = 0
    x = 0
    for row in grid[::Y]:
        if row[x] == '#':
            trees += 1

        for i in range(X):
            x += 1
            if x == len(row):
                x = 0
    return trees

# Part 2
tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for test in tests:
    total = total * Route(test[0], test[1], input)

print(Route(3, 1, input))  # Part 1 answer
print(total)  # Part 2 answer
