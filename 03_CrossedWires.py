#!/usr/bin/env python3
import csv

from shapely.geometry import LineString

"""
This whole thing is a stupid and slow solution.. 
    TODO: Use more time to plan before coding
    
PART 1
"""


# Read the strings from file
def read_wires_from_file():
    wires = []
    with open("data/03_input", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            wires.append(row)
    return wires


# Create coordinates from the strings read from the file (a line at a time)
def create_coordinates_from_wires(wire):
    tmpcords = []
    lat = 0  # U / D
    long = 0  # L / R
    tmpcords.append((lat, long))  # start
    for i in wire:
        direction = i[0]
        distance = i[1:]
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
def get_manhattan(xList, yList):
    return abs(xList[0] - yList[0]) + abs(xList[1] - yList[1])


# return all of the intersections made by the two wires + the coordinates of the wires
def get_intersections(twowires):
    wirecoordinates = []
    for i in twowires:
        wirecoordinates.append(create_coordinates_from_wires(i))

    firstwire = LineString(wirecoordinates[0])
    secondwire = LineString(wirecoordinates[1])
    return firstwire.intersection(secondwire), wirecoordinates


# get The closest manhattandistance from two wire-systems
def get_closest_manhattan_distance(twowires):
    intersections, tmp = get_intersections(twowires)

    manhattansum = []
    for point in intersections:
        manhattansum.append(get_manhattan([0, 0], [int(point.x), int(point.y)]))
    manhattansum.sort()
    return manhattansum[1]


print(get_closest_manhattan_distance(read_wires_from_file()))

"""
PART 2
"""


# returns the lowest distance to one of the intersections on the two wires
def get_closest_intersection_from_startpoint(twowires):
    intersections, wirecoordinates = get_intersections(twowires)
    distanceToIntersections = []
    for i in intersections:
        firstwirelength = LineString(wirecoordinates[0]).project(i)
        secondwirelength = LineString(wirecoordinates[1]).project(i)
        distanceToIntersections.append(firstwirelength + secondwirelength)
    distanceToIntersections.sort()
    return distanceToIntersections[1]


print(int(get_closest_intersection_from_startpoint(read_wires_from_file())))
