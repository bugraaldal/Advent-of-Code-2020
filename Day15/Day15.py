# Slow. Really slow
data = []
for x in "19,0,5,1,10,13".split(","):
    data.append(int(x))


def part1(data):
    i = 0
    spoken = []
    while i < 2020:
        if i < len(data):
            spoken.append(data[i])
        else:
            last_number = spoken[-1]
            if last_number not in spoken[:-1]:
                spoken.append(0)
            else:
                found = False
                seek_i = len(spoken) - 2
                while seek_i >= 0 and not found:
                    if spoken[seek_i] == last_number:
                        spoken.append(len(spoken) - seek_i-1)
                        found = True
                    seek_i -= 1
        i += 1
    return spoken[-1]


def last2(memo, n, turn):
    if n not in memo:
        memo[n] = (None, turn)
    else:
        memo[n] = (memo[n][1], turn)


def part2(data, n):
    memo = {}
    for i, x in enumerate(data):
        def last2(turn):
            if x not in memo:
                memo[x] = (None, turn)
            else:
                memo[x] = (memo[x][1], turn)
        last2(i+1)
    turn = len(data) + 1
    x = data[-1]
    while turn <= 30000000:
        if x in memo and not memo[x][0]:  # Occurred once
            x = 0
        else:  # Didn't occure or occured more than once
            x = memo[x][1] - memo[x][0]
        last2(turn)
        turn += 1
    return x


print(part1(data))
print(part2(data, 30000000))
