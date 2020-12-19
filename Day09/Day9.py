""" I see that I was being silly with the names. I would say this is a bad practice. """
invld = -1
prev = 25
with open("Day9.txt") as read:
    numbers = [int(i) for i in read.readlines()]

for i in range(prev, len(numbers)):
    prevs = numbers[i - prev:i]
    valid = False
    for j in range(prev):
        for k in range(prev):
            if j != k and prevs[j] + prevs[k] == numbers[i]:
                valid = True
                break
        if valid:
            break
    if not valid:
        invld = numbers[i]
        print(invld)
        break
anslist = [0]
for n in numbers:
    anslist.append(anslist[-1] + n)
for i in range(len(numbers)):
    for j in range(i + 2, len(numbers)):
        final = anslist[j + 1] - anslist[i]
        if final == invld:
            idunnohowtonamw = numbers[i:j]
            print(min(idunnohowtonamw) + max(idunnohowtonamw))
