# I don't really have anything to say about this code, I believe this one is pretty good.
def setFile(file_name):
    with open(file_name) as file:
        inputs = []
        group = []
        for line in file:
            if line != "\n":
                group.append(set(line.strip()))
            else:
                inputs.append(group)
                group = []
        inputs.append(group)
    return list(inputs)


def atLeast_yes(inputs):  # Q1 Answer
    result = 0
    for group in inputs:
        # https://en.wikipedia.org/wiki/Set_(mathematics)
        result += len(set.union(*group)) # https://stackoverflow.com/questions/31253109/how-can-i-find-the-union-on-a-list-of-sets-in-python/31253153
    return int(result)


def All_yes(inputs):  # Q2 Answer
    result = 0
    for group in inputs:
        # https://en.wikipedia.org/wiki/Set_(mathematics)
        result += len(set.intersection(*group))
    return int(result)


print("Q1:", atLeast_yes(setFile("Day6.txt")))
print("Q2:", All_yes(setFile("Day6.txt")))
