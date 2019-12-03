#!/usr/bin/env python3
import math

"""
PART 1:
"""
with open("data/01_input", "r") as f:
    masses = [line for line in f]


def divide_round_down_and_sub(number):
    return math.floor(float(number) / float(3)) - 2


total = 0
for line in masses:
    total += divide_round_down_and_sub(line)

print(total)

"""
PART 2:
"""


def calculate_fuel_for_fuel(number):
    newnumber = divide_round_down_and_sub(number)
    if newnumber <= 0:
        return 0
    return newnumber + calculate_fuel_for_fuel(newnumber)


total = 0
for line in masses:
    total += calculate_fuel_for_fuel(line)

print(total)
