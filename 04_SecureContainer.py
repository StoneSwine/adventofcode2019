from collections import Counter

"""
PART 1:
"""

part1 = 0
part2 = 0
minimum = 272091
maximum = 815432 + 1


def check_pin(pin):
    retval = False
    for i in range(1, len(pin)):
        if pin[i] < pin[i - 1]: return False
        if pin[i] == pin[i - 1]: retval = True
    return retval


"""
PART 2: 
"""


def check_pin_2(pin):
    retval = False
    for i in range(1, len(pin)):
        if pin[i] < pin[i - 1]: return False
        if any([3 > v > 1 for k, v in Counter(pin).items()]): # group and count the items
            retval = True

    return retval


for number in range(minimum, maximum):
    if check_pin(str(number)):
        part1 += 1
    if check_pin_2(str(number)):
        part2 += 1

print(part1, part2)
