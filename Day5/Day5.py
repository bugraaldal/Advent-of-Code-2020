
def P1():
    ID_Search = 0
    resultList = []
    with open("Day5.txt") as f:
        for line in f:
            row = find_row(line)
            col = find_col(line)
            ID_Search = max(ID_Search, row*8+col)
            resultList.append(row*8+col)
    print("Max id: {}".format(resultList))
    resultList.sort()
    miss = []
    for i in range(16, ID_Search-16):
        if i not in resultList:
            miss.append(i)
    print(miss)


def find_col(line):
    col = 0
    if line[7] == "R":
        col += 4
    if line[8] == "R":
        col += 2
    if line[9] == "R":
        col += 1
    return col


def find_row(line):
    row = 0
    if line[0] == "B":
        row += 64
    if line[1] == "B":
        row += 32
    if line[2] == "B":
        row += 16
    if line[3] == "B":
        row += 8
    if line[4] == "B":
        row += 4
    if line[5] == "B":
        row += 2
    if line[6] == "B":
        row += 1
    return row


def P2():
    IDs = [int(line.strip().translate(str.maketrans("BFRL", "1010")), 2)
           for line in open("Day5.txt")]
    print("Q1: {}\nQ2 {}".format(max(IDs), [
          x for x in range(max(IDs)) if x not in IDs and x+1 in IDs and x-1 in IDs])) # I wouldn't recommend this usage of one-liners.
                                                                                      # However just like Day4, I was experimenting with them.
                                                                                     
P2()
