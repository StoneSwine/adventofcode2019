#!/usr/bin/env python3

orbits = [tuple(x.strip().split(")")) for x in open("data/06_input").readlines()]
# ( A, B ) = A ) B = B ORBITS A

"""
PART 1
"""

diredge = len(orbits)


# Recursive functions is love, recursive functions is life
def get_nodes_to_com(gal):
    try:
        return [gal] + get_nodes_to_com(next(x for x in orbits if x[1] == gal[0]))
    except StopIteration:
        return [gal]


# Get indirect edges
sum = 0
for node in orbits:  # Exclude COM
    sum += len(get_nodes_to_com(node)) - 1
print(sum + (diredge))

"""
PART 2
"""
startnodes = get_nodes_to_com(next(x for x in orbits if x[1] == "YOU"))
goalnodes = get_nodes_to_com(next(x for x in orbits if x[1] == "SAN"))

# Find the shortest path between two galaxies (nodes)
startsum = goalsum = 0
for s in startnodes:
    for g in goalnodes:
        if s[0] == g[0]:
            print(startsum + goalsum)
            exit()
        goalsum += 1
    startsum += 1
    goalsum = 0
