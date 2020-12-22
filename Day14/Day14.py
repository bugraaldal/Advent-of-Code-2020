import itertools
import re
lines = []
with open("Day14.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())
# Instead of using 2 functions like part1() and part2(),
# I've used the used the part2=False in order to make the code shorter.


def run(part2=False):
    mem = {}
    for line in lines:
        if "mask" in line:
            mask = line[7:]
        else:
            maskRegex = re.findall(r"\d+", line)
            addr, val = map(int, maskRegex)
            if part2:
                k = itertools.product("01", repeat=mask.count("X"))
                iteratableMask = map(iter, k)
                for floating in iteratableMask:
                    # Joining the binaries together and adding zeros before them.
                    for m, a in zip(mask, bin(addr)[2:].zfill(36)):
                        if m == "0":
                            x = "".join(a)
                        elif m == "1":
                            x = "".join("1")
                        else:
                            next(floating)
                        mem[x] = val

            else:
                # Binary: "&" (AND) sets each bit to 1 if both bits are 1
                #         "|" (OR) sets sets each bit to 1 if one of two bits is 1
                mem[addr] = val & int(mask.replace("X", "1"), 2) | int(
                    mask.replace("X", "0"), 2)
    return sum(mem.values())


print(run())
print(run(True))
