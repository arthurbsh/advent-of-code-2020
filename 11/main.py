import time

with open("input.txt") as f:
    entries = [
        list(line)
        for line in f.read().splitlines()
    ]

def is_free(l, c, seats):
    if l == -1 or c == -1:
        return True
    try:
        return not seats[l][c] == "#"
    except:
        return True

def will_occupy(l, c, seats):
    free = 0
    for v_l in range(l-1, l+2):
        for v_c in range(c-1, c+2):
            if is_free(v_l, v_c, seats):
                free += 1
    return free == 9

def will_free(l, c, seats):
    occupied = 0
    for v_l in range(l-1, l+2):
        for v_c in range(c-1, c+2):
            if not is_free(v_l, v_c, seats):
                occupied += 1
    
    return occupied >= 5

def look_far(i):
    if i > 0:
        return i + 1
    elif i < 0:
        return i-1
    return i

def is_free2(l, c, d_l, d_c, seats):
    if l+d_l <= -1 or c+d_c <= -1:
        return True
    try:
        if seats[l + d_l][c + d_c] == ".":
            return is_free2(l, c, look_far(d_l), look_far(d_c), seats)

        return seats[l + d_l][c + d_c] == "L"
    except:
        return True

def will_occupy2(l, c, seats):
    free = 0
    for d_l in range(-1, 2):
        for d_c in range(-1, 2):
            if d_l == 0 == d_c:
                continue
            if is_free2(l, c, d_l, d_c, seats):
                free += 1
    return free == 8

def will_free2(l, c, seats):
    occupied = 0
    for d_l in range(-1, 2):
        for d_c in range(-1, 2):
            if d_l == 0 == d_c:
                continue
            is_f = is_free2(l, c, d_l, d_c, seats)
            if not is_f:
                occupied += 1
    return occupied >= 5

def part1(entries):

    current = []

    future = entries
    
    ignore = list()
    for i in entries:
        ignore.append([0] * len(i))

    while future != current:

        current = future
        future = list()

        for l in range(len(entries)):
            future.append(list())
            for c in range(len(entries[0])):
                if ignore[l][c]:
                    future[l].append(current[l][c])
                    continue
                if current[l][c] == ".":
                    ignore[l][c] = 1
                    future[l].append(".")
                elif current[l][c] == "L":
                    if will_occupy(l, c, current):
                        future[l].append("#")
                    else:
                        ignore[l][c] = 1
                        future[l].append("L")
                elif current[l][c] == "#":
                    if will_free(l, c, current):
                        future[l].append("L")
                    else:
                        ignore[l][c] = 1
                        future[l].append("#")

    occ = 0

    for i in future:
         occ += i.count("#")
            

    return occ


def part2(entries):
    current = []

    future = entries
    
    ignore = list()
    for i in entries:
        ignore.append([0] * len(i))

    while future != current:
        current = future
        future = list()

        for l in range(len(entries)):
            future.append(list())
            for c in range(len(entries[0])):
                if ignore[l][c]:
                    future[l].append(current[l][c])
                    continue
                if current[l][c] == ".":
                    future[l].append(".")
                    ignore[l][c] = 1
                elif current[l][c] == "L":
                    if will_occupy2(l, c, current):
                        future[l].append("#")
                    else:
                        future[l].append("L")
                        ignore[l][c] = 1
                elif current[l][c] == "#":
                    if will_free2(l, c, current):
                        future[l].append("L")
                    else:
                        future[l].append("#")
                        ignore[l][c] = 1

    occ = 0

    for i in future:
         occ += i.count("#")
            

    return occ

    
print("Day 11:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))