#!/usr/bin/env python3

"""
PART 1
"""


def read_numbers_into_array():
    with open("data/02_input", "r") as f:
        intcode = [int(x) for x in f.readline().split(',')]
    return intcode


def parse_intcode(intcode):
    for i in range(0, len(intcode), 4):
        if intcode[i] == 1:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        elif intcode[i] == 2:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        elif intcode[i] == 99:
            return intcode
        else:
            return intcode
    return intcode


def alert_with_values(noun, verb):
    intcode = read_numbers_into_array()
    intcode[1] = noun
    intcode[2] = verb
    return parse_intcode(intcode)[0]


print(alert_with_values(12, 2))

"""
PART 2
"""
for i in range(0, 99):
    for j in range(0, 99):
        if alert_with_values(i, j) == 19690720:
            print(str(100 * i + j))
            break
