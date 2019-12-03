#!/usr/bin/env python3
import csv
import re

from shapely.geometry import LineString

"""
PART 1
"""

# Read the strings from file
def readWiresFromFile():
    wires = []
    with open("data/03_input", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            wires.append(row)
    return wires

# Create coordinates from the strings read from the file (a line at a time)
def createCoordinatesFromWires(wire):
    regexnumbersfromletters = re.compile("([a-zA-Z]+)([0-9]+)")
    tmpcords = []
    lat = 0  # U / D
    long = 0  # L / R
    tmpcords.append((lat, long))  # start
    for i in wire:
        direction, distance = regexnumbersfromletters.match(i).groups()
        if direction == "R":
            long += int(distance)
        elif direction == "L":
            long -= int(distance)
        elif direction == "U":
            lat += int(distance)
        elif direction == "D":
            lat -= int(distance)
        tmpcords.append((lat, long))
    return tmpcords

# Return the manhattan distance between two coordinates
def getManhattan(xList, yList):
    return abs(xList[0] - yList[0]) + abs(xList[1] - yList[1])

# return all of the intersections made by the two wires + the coordinates of the wires
def getInterSections(twowires):
    wirecoordinates = []
    for i in twowires:
        wirecoordinates.append(createCoordinatesFromWires(i))

    firstwire = LineString(wirecoordinates[0])
    secondwire = LineString(wirecoordinates[1])
    return firstwire.intersection(secondwire), wirecoordinates

# get The closest manhattandistance from two wire-systems
def getClosestManhattanDistance(twowires):
    intersections, tmp = getInterSections(twowires)

    manhattansum = []
    for point in intersections:
        manhattansum.append(getManhattan([0, 0], [int(point.x), int(point.y)]))
    manhattansum.sort()
    return manhattansum[1]

assert getClosestManhattanDistance([['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]) == 6
assert getClosestManhattanDistance([['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                                    ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]) == 135
assert getClosestManhattanDistance([['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                                    ["U62", "R66", 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]) == 159

print(getClosestManhattanDistance(readWiresFromFile()))

"""
PART 2
"""
# returns the lowest distance to one of the intersections on the two wires
def getClosestIntersectionFromStartpoint(twowires):
    intersections, wirecoordinates = getInterSections(twowires)
    distanceToIntersections = []
    for i in intersections:
        firstwirelength = LineString(wirecoordinates[0]).project(i)
        secondwirelength = LineString(wirecoordinates[1]).project(i)
        distanceToIntersections.append(firstwirelength + secondwirelength)
    distanceToIntersections.sort()
    return distanceToIntersections[1]

print(int(getClosestIntersectionFromStartpoint(readWiresFromFile())))

