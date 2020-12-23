# I wonder how can I make this one shorter
# Configuring the lists and input
fields = {}
myTicket = []
ticketsNearby = []

lineRule = True
lineMine = False

with open("Day16.txt", "r") as f:
    for line in f:
        line = line.strip()

        # Checking if it is my ticket or one of the nearby tickets
        if line == "your ticket:":
            lineRule = False
            lineMine = True
            continue

        if line == "nearby tickets:":
            lineMine = False
            lineTicketsNearby = True
            continue

        if line == "":
            continue

        # Setting the tickets
        if lineRule:
            field = line[:line.index(":")]
            range1 = line[line.index(":") + 2:line.index("or ") - 1]
            range1 = [int(x) for x in range1.split("-")]
            range2 = line[line.index("or ") + 3:]
            range2 = [int(x) for x in range2.split("-")]
            fields[field] = [range1, range2]
        elif lineMine:
            myTicket = [int(x) for x in line.split(",")]
        elif lineTicketsNearby:
            ticketsNearby.append([int(x) for x in line.split(",")])

# Part 1


def validVal(Val, rules):
    for rule in rules:
        min, max = rule
        if Val >= min and Val <= max:
            return True
    return False


sum = 0
for ticket in ticketsNearby:
    for Val in ticket:
        isValid = False
        for field, rules in fields.items():
            if validVal(Val, rules):
                isValid = True
                break
        if not isValid:
            sum += Val
print(f"Part1 = {sum}")

# Part 2


def finished():
    count = 0
    for p in range(len(fieldPlace)):
        if len(fieldPlace[p]) == 1 and fieldPlace[p][0].startswith("departure"):
            count += 1
    return count == 6


invalidTickets = []
for ticket in ticketsNearby:
    for Val in ticket:
        isValid = False
        for field, rules in fields.items():
            if validVal(Val, rules):
                isValid = True
                break
        if not isValid:
            invalidTickets.append(ticket)

for ticket in invalidTickets:
    ticketsNearby.remove(ticket)


fieldPlace = []
for p in range(len(fields)):
    validfields = sorted(fields.keys())
    for ticket in ticketsNearby:
        Val = ticket[p]
        for field in list(validfields):
            if not validVal(Val, fields[field]):
                validfields.remove(field)
                break

    fieldPlace.append(validfields)

i = 0
while not finished():
    finalPos = []
    for p in range(len(fieldPlace)):
        if len(fieldPlace[p]) == 1:
            finalPos.append(fieldPlace[p][0])
    for q in range(len(fieldPlace)):
        if len(fieldPlace[q]) > 1:
            for pos in finalPos:
                if pos in fieldPlace[q]:
                    fieldPlace[q].remove(pos)
    i += 1

prod = 1
for p in range(len(fieldPlace)):
    if len(fieldPlace[p]) == 1 and fieldPlace[p][0].startswith("departure"):
        prod *= myTicket[p]
print(f"Part2 = {prod}")
