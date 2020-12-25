from functools import reduce


def same(first, second):
    final = []
    temp = set(second)
    for value in first:
        if value in temp:
            final.append(value)
    return final


data = []
with open("Day21.txt", "r") as f:
    for i in f.readlines():
        data.append(i.strip(")\n"))

foods = []
aller = {}
for line in data:
    ingredients, allergetic = line.split(" (contains ")
    ingredients = ingredients.split(" ")
    allergetic = allergetic.split(", ")
    foods.append((ingredients, allergetic))
    for allergen in allergetic:
        if allergen not in aller:
            aller[allergen] = []
        aller[allergen].append(ingredients)

everyAllergy = []
for key in aller:
    aller[key] = reduce(same, aller[key])
    everyAllergy.extend(aller[key])

# Part 1
count = 0
for food in foods:
    for ingredient in food[0]:
        if ingredient not in everyAllergy:
            count += 1
print(f"Q1: {count}")

# Part 2
actuallyAlergetic = []
toRemove = []
while len(aller):
    for key in aller:
        if len(aller[key]) == 1:
            actuallyAlergetic.append((aller[key][0], key))
            for subKey in aller:
                if subKey != key:
                    try:
                        aller[subKey].remove(aller[key][0])
                    except ValueError as e:
                        pass
            toRemove.append(key)
    for key in toRemove:
        aller.pop(key)
    toRemove = []

actuallyAlergetic.sort(key=lambda x: x[1])
actuallyAlergetic_list = []
for k in actuallyAlergetic:
    actuallyAlergetic_list.append(k[0])
actuallyAlergetic = actuallyAlergetic_list
print(f"Q2: {', '.join(actuallyAlergetic)}")
