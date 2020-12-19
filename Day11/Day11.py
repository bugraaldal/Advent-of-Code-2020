# import os
# os.chdir("/home/buura/Desktop/Python/AdventOfCode2020")
""" This must be the hardest question of all... """
import copy


def seatsFileMap():
    with open("Day11.txt", "r") as f:
        return [list(i) for i in f.read().splitlines()]


def part1():
    seats = seatsFileMap()
    finalSeats = seatsFileMap()

    dirs = [
        [-1, -1],
        [0, -1],
        [+1, -1],
        [-1, 0],
        [+1, 0],
        [-1, +1],
        [0, +1],
        [+1, +1],
    ]

    while True:
        for y in range(len(seats)):
            for x in range(len(seats[0])):
                if seats[y][x] == ".":
                    finalSeats[y][x] = "."
                    continue

                taken = 0
                for direction in dirs:
                    check_y = y + direction[1]
                    check_x = x + direction[0]

                    if check_y < 0 or check_y >= len(seats) or check_x < 0 or check_x >= len(seats[0]):
                        continue

                    seat = seats[y + direction[1]][x + direction[0]]

                    if seat == "#":
                        taken += 1

                if seats[y][x] == "L" and taken == 0:
                    finalSeats[y][x] = "#"
                elif seats[y][x] == "#" and taken >= 4:
                    finalSeats[y][x] = "L"
                else:
                    finalSeats[y][x] = seats[y][x]

        if finalSeats == seats:
            break

        seats = copy.deepcopy(finalSeats)

    allTaken = sum([row.count("#") for row in seats])

    print(allTaken)


def firstSeat(seats, x, y, x_dir, y_dir):
    check_y = y
    check_x = x

    while True:
        check_y += y_dir
        check_x += x_dir

        if check_y < 0 or check_y >= len(seats) or check_x < 0 or check_x >= len(seats[0]):
            return "L"

        check_seat = seats[check_y][check_x]

        if check_seat == "L" or check_seat == "#":
            return check_seat


def part2():
    seats = seatsFileMap()
    finalSeats = seatsFileMap()

    dirs = [
        [-1, -1],
        [0, -1],
        [+1, -1],
        [-1, 0],
        [+1, 0],
        [-1, +1],
        [0, +1],
        [+1, +1],
    ]

    while True:
        for y in range(len(seats)):
            for x in range(len(seats[0])):
                if seats[y][x] == ".":
                    finalSeats[y][x] = "."
                    continue

                taken = 0
                for direction in dirs:

                    first_visible_seat = firstSeat(
                        seats, x, y, direction[0], direction[1])

                    if first_visible_seat == "#":
                        taken += 1

                if seats[y][x] == "L" and taken == 0:
                    finalSeats[y][x] = "#"
                elif seats[y][x] == "#" and taken >= 5:
                    finalSeats[y][x] = "L"
                else:
                    finalSeats[y][x] = seats[y][x]

        if finalSeats == seats:
            break

        seats = copy.deepcopy(finalSeats)

    allTaken = sum([row.count("#") for row in seats])

    print(allTaken)


part1()
part2()
