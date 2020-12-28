from copy import copy

_input = [10705932, 12301431]
subject_number = 7
# Card loop size
val = 1
cardSize = 0
while val != _input[0]:
    val *= subject_number
    val = val % 20201227
    cardSize += 1

# Door loop size
val = 1
doorSize = 0

while val != _input[1]:
    val *= subject_number
    val = val % 20201227
    doorSize += 1
# Encrypt key door
val_door = 1
for _ in range(cardSize):
    val_door *= _input[1]
    val_door = val_door % 20201227

# Encrypy key card
val_card = 1
for _ in range(doorSize):
    val_card *= _input[0]
    val_card = val_card % 20201227
print(f"Q1: {val_card}")
""" There is no part 2. It got me. I almost got emotional """
print("Congrats! 50 stars")
