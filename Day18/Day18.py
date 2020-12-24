# I wouldn't be able to say if this question was hard or easy. It uses the fundamental stuff. No modules.
# However changing the rules of math was mind-boggling
def Part1(part2):
    calc = list()

    with open("Day18.txt") as f:
        for line in f:
            operation = line.strip().replace(" ", "")

            start = 0
            parentheses = list()

            while(True):
                # Taking the parenthesis and removing (.pop()) them from the list
                for i in range(start, len(operation)):
                    if operation[i] == "(":
                        parentheses.append(i)
                    elif operation[i] == ")":
                        parenthsis_i = parentheses.pop()
                        # Calling the change function in order the change the laws of the math
                        val = change(operation[parenthsis_i+1:i], part2)
                        start = parenthsis_i

                        operation = operation[:parenthsis_i] + \
                            str(val) + operation[i+1:]
                        break

                if operation.count("(") == 0:
                    calc.append(change(operation, part2))
                    break

    return sum(calc)

# The function that does it all


def change(operation, part2):
    n = 0

    while(True):
        opi = -1
        op = None

        opfound = False

        if part2:
            n1i = 0
        n2i = -1

        for i, c in enumerate(operation):
            if c == "+" or c == "*":
                if opfound:
                    n2i = i
                    break
                else:
                    if part2:
                        if not (c == "+" or operation.count("+") == 0):
                            n1i = i + 1
                        else:
                            opfound = True
                            opi = i
                            op = c
                    else:
                        opfound = True
                        opi = i
                        op = c

            if i == len(operation) - 1:
                n2i = i + 1
        if part2:
            n1 = int(operation[n1i:opi])
            n2 = int(operation[opi+1:n2i])
        else:
            n1 = int(operation[0:opi])
            n2 = 0
            n2 = int(operation[opi+1:n2i])

        if op == "+":
            n = n1 + n2
        elif op == "*":
            n = n1 * n2

        if part2:
            operation = operation[:n1i] + str(n) + operation[n2i:]
            if operation.count("+") + operation.count("*") == 0:
                return n

        else:
            if len(operation[n2i:]) == 0:
                return n
            operation = str(n) + operation[n2i:]


print(f"Q1: {Part1(False)}")
print(f"Q2: {Part1(True)}")
