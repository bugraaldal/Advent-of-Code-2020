
def setRule(ruleID, val):
    rule = rules[ruleID]
    if rule.startswith('"'):
        if not val:
            return []
        return [val[1:]] if rule[1] == val[0] else []
    possible = []
    # Splitting the rule for the sub-rules.
    for option in rule.split(" | "):
        newPossible = [val]
        for rID in option.split(" "):
            newPossible = [newPoss for currentPossible in newPossible for newPoss in setRule(
                rID, currentPossible)]

        possible += newPossible
    return possible


# Configuring the input
messages = []
with open("Day19.txt") as f:
    arange = f.read().split("\n\n")

rules = dict(map(lambda s: s.split(": "), arange[0].split("\n")))
for i in arange[1].split("\n"):
    messages.append(i)
# Part 1
answer1 = []
for mssge in messages:
    if "" in setRule("0", mssge):
        answer1.append(1)
print(f"Q1: {sum(answer1)}")

# Part2
# Setting the requirement of part 2
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
answer2 = []
for mssge in messages:
    if "" in setRule("0", mssge):
        answer2.append(1)
print(f"Q2: {sum(answer2)}")
