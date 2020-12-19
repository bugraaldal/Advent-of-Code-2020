#import os
#os.chdir("/home/buura/Desktop/Python/AdventOfCode2020")
""" I turns out I've deleted the second part's answer, so I had to come up with it again.
    I've actually used a brute force approach at first. Then changed it in an attempt to find a more efficent solution. """
    
import copy
# Setting up some lists in order to jump back and forth in the input lists easily
answers = []
other = []
numlist = []
loopviaawans = 0
res = 0
loop = []
with open("Day8.txt", "r") as f:
    K = f.readlines()
    for item in K:
        answers.append(item.split(" "))
for everyitem in answers:
    other.append(everyitem[1].replace("\n", ""))
numlist = list(map(int, other))

# Part 1 solution
def part1(loopviaawans, res):
    while True:
        # Checks if there is "Checked" word in the input and if there is, stops the loop
        if "Checked" in answers[loopviaawans]:
            print(res)
            break
        # Applies the instructions and adds "Checked" to each visited instruction line
        elif "jmp" in answers[loopviaawans]:
            answers[loopviaawans].append("Checked")
            loopviaawans = loopviaawans+(numlist[loopviaawans])

        elif "acc" in answers[loopviaawans]:
            res += numlist[loopviaawans]
            answers[loopviaawans].append("Checked")
            loopviaawans += 1
        elif "nop" in answers[loopviaawans][0]:
            answers[loopviaawans].append("Checked")
            loopviaawans += 1


part1(0, 0)


# Using all as a variable name is a really bad practice since there is already a method called all()
with open("Day8.txt", "r") as f:
    all = f.read().splitlines()


def part_two(all):
    for i in range(len(all)):
        allCopy = copy.deepcopy(all) # If not copied the program outputs a wrong answer
        # Changing the "jmp"s with "nop"s.
        if allCopy[i].split()[0] == "jmp":
            allCopy[i] = allCopy[i].replace("jmp", "nop")
        elif allCopy[i].split()[0] == "nop":
            allCopy[i] = allCopy[i].replace("nop", "jmp")

        acc = 0
        idx_list = [False for i in allCopy]
        idx = 0
        operation = allCopy[idx]
        while True:
            idx_list[idx] = True
            op, value = operation.split()

            if op == "nop":
                idx += 1
            elif op == "jmp":
                idx += int(value)
            elif op == "acc":
                acc += int(value)
                idx += 1

            if idx_list[idx] == True:
                break
            if idx == (len(allCopy) - 1):
                return acc
            operation = allCopy[idx]


print(part_two(all))
