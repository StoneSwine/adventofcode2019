#!/usr/bin/env python3

def get_pmode(number):
    opc = (number // 1) % 10
    m1 = (number // 100) % 10
    m2 = (number // 1000) % 10
    return [opc, m1, m2]


def get_value(ico, param, mode):
    return param if mode else ico[param]


def run(input):
    pos = 0
    ico = [int(x) for x in open("data/05_input", "r").readline().split(",")]

    while pos <= len(ico):
        fullopc = ico[pos]
        p1, p2, p3 = (ico[pos + 1:pos + 4] if pos <= len(ico) - 4 else [1, 1, 1])
        [opc, m1, m2] = get_pmode(ico[pos])

        if opc == 1:
            ico[p3] = get_value(ico, p1, m1) + get_value(ico, p2, m2)
            pos += 4
        elif opc == 2:
            ico[p3] = get_value(ico, p1, m1) * get_value(ico, p2, m2)
            pos += 4
        elif opc == 3:
            ico[p1] = input
            pos += 2
        elif opc == 4:
            print(get_value(ico, p1, m1))
            pos += 2
        elif opc == 5:
            if get_value(ico, p1, m1) != 0:
                pos = get_value(ico, p2, m2)
            else:
                pos += 3
        elif opc == 6:
            if get_value(ico, p1, m1) == 0:
                pos = get_value(ico, p2, m2)
            else:
                pos += 3
        elif opc == 7:
            ico[p3] = (1 if get_value(ico, p1, m1) < get_value(ico, p2, m2) else 0)
            pos += 4
        elif opc == 8:
            ico[p3] = (1 if get_value(ico, p1, m1) == get_value(ico, p2, m2) else 0)
            pos += 4
        elif fullopc == 99:
            return
        else:
            print(fullopc)


run(1)
run(5)
