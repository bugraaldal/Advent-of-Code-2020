""" There is no need for this much lists. It could have been done with less lists and the code would be clearer, however this whole
thinng is about seeing my growth over time. Therefore I'm keeping it """
InputList = []
new_list = []
final_list = []
RangeList = []
wordList = []
Passwords = []
Words = []
with open("Day2.txt", "r") as f:
    for line in f:
        InputList.append(line)
# Setting up the lists
for ch in InputList:
    new = ch.replace("\n", "")
    new_list.append(new)
for i in new_list:
    final_list.append(i.split(":"))
for each in final_list:
    wordList.append(each[0].split())
# Seperating lists into three parts, range, character and the password
for eachOne in wordList:
    RangeList.append(eachOne[0].split("-"))
for eachItem in final_list:
    Passwords.append(eachItem[1])
for k in wordList:
    Words.append(k[1])

valid = 0  # Part 1 answer
x = 0  # Part 2 answer
for password, word, num in zip(Passwords, Words, RangeList):
    lil = int(num[0])
    big = int(num[1])
    if password.count(word) <= big and password.count(word) >= lil:
        valid += 1
    if (password[lil] == word or password[big] == word) and password[lil] != password[big]:
        x += 1
print(valid)
print(x)

