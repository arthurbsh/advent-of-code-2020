with open("input.txt") as f:
    entries = [
        int(line)
        for line in f.read().splitlines()
    ]

def is_valid_sum(value, preamble):
    for i in preamble:
        for j in preamble:
            if i+j ==  value:
                return True

    return False

def part1(entries):
    for i in range(25, len(entries)):
        if not is_valid_sum(entries[i], entries[i-25:i]):
            return entries[i]

def part2(entries):
    invalid = part1(entries)
    found = False

    for i in range(len(entries)):
        for j in range(len(entries)):
            if sum(entries[i:j]) > invalid:
                break
            elif sum(entries[i:j]) == invalid:
                found = True
                break

        if found:
            break
    
    return min(entries[i:j]) + max(entries[i:j])

print("Day 9:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))