from collections import Counter

part1 = 0
part2 = 0
minimum = 272091
maximum = 815432 + 1


def check_pin(pin):
    firstpart = secondpart = False
    for i in range(1, len(pin)):
        if pin[i] < pin[i - 1]:
            return False, False
        if pin[i] == pin[i - 1]:
            firstpart = True

    if any([3 > v > 1 for k, v in Counter(pin).items()]):  # group and count the items
        secondpart = True

    return firstpart, secondpart


for number in range(minimum, maximum):
    firstpart, secondpart = check_pin(str(number))
    if firstpart:
        part1 += 1
    if secondpart:
        part2 += 1

print(part1, part2)