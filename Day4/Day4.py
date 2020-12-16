""" I had to dive deeper to the regex module for this question. This was quite hard...
  Also I've experimented with one-liners! """
import re
with open("Day4.txt", "r") as f:
        inputList = f.read().split("\n\n")
# Part 1:
seekfor = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
print(sum(all(i in each for i in seekfor)for each in inputList))
# Part 2:
fields = {
    "byr": "19[2-9][0-9]|200[0-2]",
    "iyr": "201[0-9]|2020",
    "eyr": "202[0-9]|2030",
    "hgt": "(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in",
    "hcl": "#[0-9a-f]{6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "[0-9]{9}"
}
fields = [re.compile(fr"\b{k}:({v})\b") for k, v in fields.items()]
count = sum(all(x.search(line) for x in fields) for line in inputList)
print(count)
