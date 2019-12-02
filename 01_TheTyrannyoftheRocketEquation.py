#!/usr/bin/env python3
import math

"""
PART 1:
"""
with open("data/01_input", "r") as f:
    masses = [line for line in f]

def divideRoundDownAndSub(number):
    return math.floor(float(number)/float(3))-2

assert divideRoundDownAndSub(12) == 2
assert divideRoundDownAndSub(14) == 2
assert divideRoundDownAndSub(1969) == 654
assert divideRoundDownAndSub(100756) == 33583

sum = 0
for line in masses:
    sum += divideRoundDownAndSub(line)

print(sum)

"""
PART 2:
"""
def calculateFuelForFuelRecursive(number):
    newnumber = divideRoundDownAndSub(number)
    if newnumber <= 0:
        return 0
    return newnumber + calculateFuelForFuelRecursive(newnumber)

assert calculateFuelForFuelRecursive(100756) == 50346

sum = 0
for line in masses:
    sum += calculateFuelForFuelRecursive(line)

print(sum)