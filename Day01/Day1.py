#I have used a very complicated while loop for the part 2, instead of just using two for loops. I wouldn't recommend doing this.
InputList = []
new_list = []
with open("Day1.txt", "r") as f:
    for line in f:
        InputList.append(line)
for ch in InputList:
    new = ch.replace("\n", "")
    new_list.append(new)
new_list = list(map(int, new_list))

def part1():
    x = 0
    y = 1
    while True:
        try:
            if new_list[x] + new_list[y] == 2020:
                print(new_list[x]*new_list[y])
                break
            else:
                y += 1
        except IndexError:
            x += 1
            y = x+1


def part2():
    x = 0
    y = 1
    z = 2
    while True:
        try:
            if new_list[x] + new_list[y] + new_list[z] == 2020:
                print(new_list[x], new_list[y], new_list[z])
                break
            else:
                z += 1
        except IndexError:
            y += 1
            z = y + 1
            try:
                if new_list[x] + new_list[y] + new_list[z] == 2020:
                    print(new_list[x], new_list[y], new_list[z])
                    break
                else:
                    z += 1
            except IndexError:
                x += 1
                y = x + 1
                z = y + 1
                if new_list[x] + new_list[y] + new_list[z] == 2020:
                    print(new_list[x], new_list[y], new_list[z])
                    break
    print(new_list[x]*new_list[y]*new_list[z])



part1()
part2()
