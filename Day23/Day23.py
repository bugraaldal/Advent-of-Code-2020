# Place picked up cups next to destination cup
def rmve(cup, i, maxCup):
    removeCup1 = i[cup]
    removeCup2 = i[removeCup1]
    removeCup3 = i[removeCup2]
    # Advance current cup
    _next = i[removeCup3]
    i[cup] = _next

    destination = cup
    while True:
        destination = destination - 1
        if destination == 0:
            destination = maxCup
        if destination not in [removeCup1, removeCup2, removeCup3]:
            break

    _next = i[destination]
    i[destination] = removeCup1
    i[removeCup3] = _next


def game(cups, turns):

    # Index of cup to next cup
    count = len(cups)
    i = [None] * (count+1)
    for q, c in enumerate(cups):
        i[c] = cups[(q + 1) % count]

    cup = cups[0]
    maxCup = max(cups)
    for _ in range(0, turns):
        rmve(cup, i, maxCup)
        cup = i[cup]

    return i


cups = [int(c) for c in "952316487"]  # input


def part1():
    global cups
    i = game(cups, 100)

    result = []
    next1 = i[1]
    while next1 != 1:
        result.append(str(next1))
        next1 = i[next1]
    print("Q1:", "".join(result))

# Add 1 million cups


def part2():
    global cups
    cups.extend(range(10, 1000001))
    i = game(cups, 10000000)

    next1 = i[1]
    next2 = i[next1]
    print("Q2:", next1 * next2)


part1()
part2()
