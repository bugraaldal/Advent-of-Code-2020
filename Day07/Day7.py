""" Day 7 was by far the hardest one compared to the others. 
  Not like the coding part, I was pretty fast at that but coming up with it's algorithm
  was really hard. I remember struggling a lot although I knew the second part beforehand. 
  At least I was able to code faster since I came up with both part one and two's answer at once. """
# import os
# os.chdir("/home/buura/Desktop/Python/AdventOfCode2020")


def parse(item):
    item = item.strip().strip(".s")[: -len(" bag")].split(" ", 1)
    item[0] = int(item[0])
    return item


rules = {}
wanted = "shiny gold"

with open("Day7.txt", "r") as f:
    for line in f:
        line = line.strip()
        container, contents = line.split("bags", 1)
        container = container.strip()

        contents = contents.strip()[len("contain "):]
        if contents.startswith("no"):
            contents = []
        else:
            contents = [parse(item) for item in contents.split(",")]

        rules[container] = contents


def part1():
    has_wanted = set()

    while True:
        new_addition = False
        for container, contents in rules.items():
            if container in has_wanted:
                continue
            simple_contents = [item[1] for item in contents]
            if wanted in simple_contents:
                has_wanted.add(container)
                new_addition = True
            for item in simple_contents:
                if item in has_wanted:
                    has_wanted.add(container)
                    new_addition = True
        if not new_addition:
            break

    print(len(has_wanted))


def count_bags(container):
    total = 0
    for item in rules[container]:
        total += item[0] * (1 + count_bags(item[1]))
    return total


def part2():
    print(count_bags(wanted))


part1()
part2()
