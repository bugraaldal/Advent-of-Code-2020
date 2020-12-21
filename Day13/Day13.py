""" I wouldn't be able to pass this day without the community. I didn't know the "Chinese Remainder Theorem". """
# Set the input
buses = []
orderBus = []

with open("Day13.txt", "r") as f:
    start = int(f.readline().strip())
    for bus in f.readline().strip().split(","):
        if bus == "x":
            orderBus.append(None)
            continue
        bus = int(bus)
        buses.append(bus)
        orderBus.append(bus)


def part1():
    # Setting up the key for the min() function
    def waitTime(bus):
        return -(start % -bus)
    earliest = min(buses, key=waitTime)
    print(earliest * waitTime(earliest))


# Part 2
# Highly based on other people

# List orderBus to a dict
def orderBusDict():
    return {delay: bus for delay, bus in enumerate(orderBus) if bus is not None}

def get_mods():
    mods = ((bus, (bus - delay) % bus)
            for delay, bus in orderBusDict().items())
    mods = sorted(mods, reverse=True)
    return mods


# I am told about this, wouldn't be able come up with this on my own
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem


def part2_ChineseRemainder():
    x = 0
    step = 1
    for div, rmndr in get_mods():
        while x % div != rmndr:
            x += step

        step *= div
    print(x)


part1()
part2_ChineseRemainder()


# This is my actual answer but isn't usable since the actual input is so long to execute this function.
# Works for shorter -example- inputs.
def solPart2Slow():
    def part2():
        import itertools
        for time in itertools.count(buses[0], buses[0]):
            for delay, bus in orderBusDict().items():
                if (time + delay) % bus != 0:
                    break
            else:
                return time
    part2()


#print(solPart2Slow())
