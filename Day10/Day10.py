# I am very proud of this.
with open("Day10.txt","r") as f:
  lines = list(map(int, f.read().split('\n')))
  lines = lines + [0, max(lines)+3]
  lines.sort()


ZeroList = [0, 0, 0]
for i in range(len(lines) - 1):
    ZeroList[lines[i+1] - lines[i]-1] += 1
print(ZeroList[0]*ZeroList[-1])


def tie(lines, i):
    answer = 0
    if x[i] != -1:
        return x[i]
    if i == len(lines) - 1:
        return 1
    for j in range(i+1, len(lines)):
        if lines[j] - lines[i] < 4:
            answer += tie(lines, j)
    x[i] = answer
    return answer


x = [-1 for _ in range(len(lines))]
print(tie(lines, 0))
