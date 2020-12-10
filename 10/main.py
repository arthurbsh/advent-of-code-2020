with open("input.txt") as f:
    entries = [
        int(line)
        for line in f.read().splitlines()
    ]

entries.append(0)
entries.sort()
entries.append(entries[len(entries) - 1 ] + 3)

def part1(entries):
    diff_1 = 0
    diff_3 = 0
    
    for i in range(len(entries) - 1):
        if entries[i+1] -  entries[i] == 1:
            diff_1 += 1
        elif entries[i+1] -  entries[i] == 3:
            diff_3 += 1
        elif entries[i+1] -  entries[i] > 3:
            break
    
    return diff_1 * diff_3

def variations(adapters):
    length = len(adapters)
    
    if length <= 2:
        return 1
    elif length == 3:
        return 2
    elif length == 4:
        return 4
    elif length == 5:
        return 7

def part2(entries):
    split_3 = list()
    current_group = list()

    for i in range(len(entries) - 1):
        current_group.append(entries[i])

        if entries[i+1] -  entries[i] == 3:
            split_3.append(current_group)
            current_group = list()

    result = 1

    for l in split_3:
        result *= variations(l)

    return result

    

print("Day 10:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))